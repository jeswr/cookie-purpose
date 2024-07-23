import json
import re
from db import connection

data=json.loads(open('data/translations.json', "r").read())
purposes:list[str]=[]

def normalize(item: str):
  item=re.sub('cookies?$', '', re.sub('(-| |\\.|\\:)+$', '', item.replace(' & ', ' and ')))
  return data[item[1:]] if item[1:] in data else item

for item, in connection.cursor().execute("SELECT DISTINCT purpose FROM consent_data").fetchall():
  if item:
    purposes.append(normalize(item))
