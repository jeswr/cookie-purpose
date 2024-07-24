import os

# Get the directory of the current module
module_dir = os.path.dirname(__file__)
purposes_doc=open(os.path.join(module_dir, "purposes.tsv"), 'r').read()
