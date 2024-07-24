from cached_path import cached_path
import os

# Get the directory of the current module
module_dir = os.path.dirname(__file__)

db_path=cached_path("https://zenodo.org/records/5838646/files/datasets.zip?download=1!04_Cookie_Databases/tranco_05May_20210510_201615.sqlite", extract_archive=True, cache_dir=os.path.join(module_dir, '.cache'))
