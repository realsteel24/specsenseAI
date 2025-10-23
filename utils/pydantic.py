
from pydantic import BaseModel, Field, ValidationError
from langchain_core.output_parsers import PydanticOutputParser


# Define Pydantic model for output parsing
class SpecItem(BaseModel):
    hard_spec: str = Field(..., description="The specs that the use must compulsorily have.")
    soft_needs: str = Field(..., description="The specs that the user would like to have but are not compulsory.")
    reason: str = Field(..., description="The reason for recommendation")


def get_parser():
    parser = PydanticOutputParser(pydantic_object=SpecItem)
    format_instructions = parser.get_format_instructions()

    return parser, format_instructions


