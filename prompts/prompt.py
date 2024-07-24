import os
from langchain.prompts import PromptTemplate
from ..parser.purpose import output_parser
from .purposes import purposes_doc

# Get the directory of the current module
module_dir = os.path.dirname(__file__)

prompt_template = PromptTemplate(
    input_variables=["name", "category", "description", "purposes", "format_instructions"],
    partial_variables={
        "purposes": purposes_doc,
        "format_instructions": output_parser.get_format_instructions()
      },
    template=open(os.path.join(module_dir, "prompt.fstring"), 'r').read()
)
