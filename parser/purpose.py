from typing import List, Optional
from pydantic import BaseModel, Field, conlist, conint
from langchain.output_parsers import PydanticOutputParser
from ..prompts.purposes import purposes_doc

_, name, definition, scope_note = purposes_doc.splitlines()[11].split("\t")
le=len(purposes_doc.splitlines()) - 1

class UnmatchedConcept(BaseModel):
    name: str = Field(description=f"The name of the concept that was not available e.g. {name}.")
    definition: str = Field(description=f"The definition of the concept that was not available e.g. {definition}.")
    scopeNote: Optional[str] = Field(description=f"A description of the scope for which the concept applies e.g. {scope_note}.")
    subsetOf: conlist(conint(ge=1, le=le)) = Field(description="An array of numbers representing the line indices of the terms that are a superset of this concept.")
    supersetOf: conlist(conint(ge=1, le=le)) = Field(description="An array of numbers representing the line indices of the terms that are a subset of this concept.")

class PurposesSchema(BaseModel):
    explanation: str = Field(description="A precise explanation of the reasoning behind the answer. DO NOT quote the prompt in this field.")
    results: conlist(conint(ge=1, le=le)) = Field(description="An array of numbers representing the line indices of the terms that apply to the description.")
    unmatchedConcepts: list[UnmatchedConcept] = Field(description="An array of concepts in the description that were not available - these should NOT be tied to a particular product. If the concept is a refinement of another concept, please still add it here, and provide the line indices of the superset concepts. For instance, if the description is \"Cookie consent system cookie for storing the level of cookie consent.\", then one of the unmatchedConcepts would be {name: \"Cookie consent system cookie\", definition: \"A cookie for storing the level of cookie consent.\", subsetOf: [37]}.")

# Define the output parser
output_parser = PydanticOutputParser(pydantic_object=PurposesSchema)
