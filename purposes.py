import json, re, sqlite3, os
from .db import db_path
from joblib import Memory

from .embeddings import embedder
from .db import db_path
import numpy as np
from sklearn.cluster import DBSCAN

# Get the directory of the current module
module_dir = os.path.dirname(__file__)

data=json.loads(open(os.path.join(module_dir, 'data/translations.json'), "r").read())
memory = Memory(os.path.join(module_dir, '.cache'))

def normalize(item: str):
  item=data[item[1:-1]] if item[1:-1] in data else item
  item=re.sub('cookies?$', '', re.sub('(-| |\\.|\\:)+$', '', item.replace(' & ', ' and ')))
  item=data[item[1:-1]] if item[1:-1] in data else item
  return item

@memory.cache
def get_purposes():
  connection=sqlite3.connect(db_path)
  purposes_list:list[str]=[]

  for item, in connection.cursor().execute("SELECT DISTINCT purpose FROM consent_data").fetchall():
    if item:
      purposes_list.append(normalize(item))

  purposes_list = list(set(purposes_list))
  lower_purposes = [e.lower() for e in purposes_list]

  return [ purposes_list[i] for i in range(len(purposes_list)) if lower_purposes[i] not in lower_purposes[:i] ]

@memory.cache
def get_filtered_purposes():
  purposes=get_purposes()
  embeddings=np.array(embedder.embed_documents(purposes)).astype('float32')

  # TODO: Tweak espilon
  dbscan = DBSCAN(eps=0.15, min_samples=2)
  labels = dbscan.fit_predict(embeddings)

  np_purposes = np.array(purposes)
  new_purposes = list(np_purposes[labels == -1])

  for i in range(0, max(labels)):
    new_purposes.append(np_purposes[labels == i][0])

  return new_purposes
