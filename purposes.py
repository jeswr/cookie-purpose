from ast import List
from cached_path import cached_path
import sqlite3
import json
import re

path=cached_path("https://zenodo.org/records/5838646/files/datasets.zip?download=1!04_Cookie_Databases/tranco_05May_20210510_201615.sqlite", extract_archive=True, cache_dir='./.cache')
con=sqlite3.connect(path)
data=json.loads(open('translations.json', "r").read())
purposes:list[str]=[]

for item, in con.cursor().execute("SELECT DISTINCT purpose FROM consent_data").fetchall():
  if item:
    item=re.sub('cookies?$', '', re.sub('(-| |\\.|\\:)+$', '', item.replace(' & ', ' and ')))
    purposes.append(data[item[1:]] if item[1:] in data else item)
