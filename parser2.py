# from langchain import LangChain
from unittest import result
from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from embeddings import model
from typing import List

# TODO: Include retry parser
# https://python.langchain.com/v0.1/docs/modules/model_io/output_parsers/types/retry/

# Define the nested data structure with Pydantic
class SubItem(BaseModel):
    name: str
    value: str

class NestedObject(BaseModel):
    id: str
    items: List[SubItem]

# Define the prompt
prompt_template = PromptTemplate(
    input_variables=["name", "category", "description", "purposes", "format_instructions"],
    partial_variables={
        "purposes": open('templates/purposes.tsv', 'r').read(),
        "format_instructions": ""
      },
    template=open('templates/prompt.fstring', 'r').read()
)

# Define the output parser
output_parser = PydanticOutputParser(pydantic_object=NestedObject)

chain = prompt_template | model | output_parser

chain.invoke({"id": "3"})

# Create the chain
# chain = LLMChain(
#     prompt=prompt_template,
#     llm=LangChain.llms.OpenAI(),
#     output_parser=output_parser
# )

# Run the chain
# input_data = {"id": "123"}
# result = chain(input_data)
res=output_parser.parse("{\"id\": \"3\", \"items\": [{ \"name\": \"betty\", \"value\": \"4\", \"t\": \"t\" }, { \"name\": \"betty\", \"value\": \"7\", \"t\": \"t\" }]}")
print(res.items[0].value == "4")
