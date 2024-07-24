import sqlite3
from dotenv import load_dotenv
load_dotenv()

from .requestDebugger import debug_requests_on
# debug_requests_on()

from .prompts.prompt import prompt_template
from .embeddings import model, embedder
from .parser.purpose import output_parser
from .db import db_path
from .purposes import purposes
from langchain_community.callbacks import get_openai_callback

chain = prompt_template | model | output_parser

connection=sqlite3.connect(db_path)

# print(connection.cursor().execute(f'PRAGMA table_info(consent_data)').fetchall())
# connection.cursor().execute('SELECT COLUMNS FROM consent_data ;')

# for item, purpose in connection.cursor().execute("SELECT * FROM sys.columns WHERE object_id = OBJECT_ID('dbo.consent_data') ").fetchall():
#   print(item, purpose)
#   exit()
#  name purpose

# batches=[{ "name": name, "description": normalize(purpose), "category": cat_name } for name, purpose, cat_name in connection.cursor().execute("SELECT name, purpose, cat_name FROM consent_data").fetchall()[:5]]
# for res in chain.batch(batches):
#   print(res)
#   exit()
# print(res)

# print(len(purposes))
# exit()

with get_openai_callback() as cb:

  embedding = embedder.embed_documents(purposes)

  # for name, purpose, cat_name in connection.cursor().execute("SELECT name, purpose, cat_name FROM consent_data").fetchall()[:1]:
  #   print('---')
  #   res = chain.batch([{ "name": name, "description": purpose, "category": cat_name }])
  #   print(name, purpose, res)

  print(f"Total Tokens: {cb.total_tokens}")
  print(f"Prompt Tokens: {cb.prompt_tokens}")
  print(f"Completion Tokens: {cb.completion_tokens}")
  print(f"Total Cost (USD): ${cb.total_cost}")
  # print(f"Total Cost (USD): ${cb.}")
