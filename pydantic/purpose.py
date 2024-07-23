from typing import List, Optional
from pydantic import BaseModel, Field

class UnmatchedConcept(BaseModel):
    name: str = Field(description="The name of the concept that was not available e.g. \"concept_name\".")
    definition: str = Field(description="The definition of the concept that was not available e.g. \"concept_definition\".")
    scopeNote: Optional[str] = Field(description="A description of the scope for which the concept applies e.g. \"scope_note\".")
    subsetOf: List[int] = Field(ge=1, le=95, description="An array of numbers representing the line indices of the terms that are a superset of this concept.")

class PurposesSchema(BaseModel):
    explanation: str = Field(description="A precise explanation of the reasoning behind the answer. DO NOT quote the prompt in this field.")
    results: List[int] = Field(ge=1, le=95, description="An array of numbers representing the line indices of the terms that apply to the description.")
    unmatchedConcepts: List[UnmatchedConcept] = Field(description="An array of concepts in the description that were not available - these should NOT be tied to a particular product. If the concept is a refinement of another concept, please still add it here, and provide the line indices of the superset concepts. For instance, if the description is \"Cookie consent system cookie for storing the level of cookie consent.\", then one of the unmatchedConcepts would be {name: \"Cookie consent system cookie\", definition: \"A cookie for storing the level of cookie consent.\", subsetOf: [37]}.")
