from cached_path import cached_path
import sqlite3

path=cached_path("https://zenodo.org/records/5838646/files/datasets.zip?download=1!04_Cookie_Databases/tranco_05May_20210510_201615.sqlite", extract_archive=True, cache_dir='./.cache')
connection=sqlite3.connect(path)
