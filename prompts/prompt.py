from langchain.prompts import PromptTemplate
from ..pydantic.purpose import output_parser

prompt_template = PromptTemplate(
    input_variables=["name", "category", "description", "purposes", "format_instructions"],
    partial_variables={
        "purposes": open('templates/purposes.tsv', 'r').read(),
        "format_instructions": output_parser.get_format_instructions()
      },
    template=open('templates/prompt.fstring', 'r').read()
)
