from dotenv import load_dotenv
load_dotenv()

from requestDebugger import debug_requests_on
debug_requests_on()

from .prompts.prompt import prompt_template
from .embeddings import model
from .pydantic.purpose import output_parser
from .db import connection
from .purposes import normalize

chain = prompt_template | model | output_parser


