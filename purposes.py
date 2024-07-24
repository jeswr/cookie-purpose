import json, re, sqlite3, os
from .db import db_path

# Get the directory of the current module
module_dir = os.path.dirname(__file__)

data=json.loads(open(os.path.join(module_dir, 'data/translations.json'), "r").read())
purposes:list[str]=[]

def normalize(item: str):
  item=data[item[1:-1]] if item[1:-1] in data else item
  item=re.sub('cookies?$', '', re.sub('(-| |\\.|\\:)+$', '', item.replace(' & ', ' and ')))
  item=data[item[1:-1]] if item[1:-1] in data else item
  return item

connection=sqlite3.connect(db_path)

for item, in connection.cursor().execute("SELECT DISTINCT purpose FROM consent_data").fetchall():
  if item:
    purposes.append(normalize(item))

purposes = list(set(purposes))
lower_purposes = [e.lower() for e in purposes]

purposes_clean = [ purposes[i] for i in range(len(purposes)) if lower_purposes[i] not in lower_purposes[:i] ]
purposes = purposes_clean
