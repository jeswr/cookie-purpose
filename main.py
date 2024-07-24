import sqlite3
from time import sleep
from dotenv import load_dotenv
load_dotenv()

from .requestDebugger import debug_requests_on
# debug_requests_on()

from .prompts.prompt import prompt_template
from .embeddings import model
from .parser.purpose import output_parser
from .db import db_path
from .purposes import get_filtered_purposes
from langchain_community.callbacks import get_openai_callback
from sklearn.cluster import DBSCAN
import json

chain = prompt_template | model | output_parser

# connection=sqlite3.connect(db_path)

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
tasks = []

def create_task(id: int, message: str):
    return {
        "custom_id": f"task-{id}",
        "method": "POST",
        "url": "/v1/chat/completions",
        "body": {
            "model": "gpt-4o-mini",
            "temperature": 0,
            "response_format": { 
                "type": "json_object"
            },
            "messages": [
                {
                    "role": "user",
                    "content": message
                }
            ],
        }
    }

with get_openai_callback() as cb:
  new_purposes = get_filtered_purposes()
  i = 0

  print('writing ...')
#   with open(f"cookie-purpose/batch_purposes_{i}.jsonl", 'w') as file:
#   for purpose in new_purposes[:1000]:
#     # i += 1
#     # if i > 500:
#     #   break
#     res = chain.invoke({ "description": purpose })
    

#     # print(f"Total Tokens: {cb.total_tokens}")
#     # print(f"Prompt Tokens: {cb.prompt_tokens}")
#     # print(f"Completion Tokens: {cb.completion_tokens}")
#     i += 1
#     print(f"[{i}] Cost: ${cb.total_cost} | Total Tokens: {cb.total_tokens}")
#     break
  chain.batch(new_purposes, { "max_concurrency": 5 })
#   while i < len(new_purposes):
#     batch = new_purposes[i:i+50]
#     chain.batch(batch, { "max_concurrency": 5 })
#     i += 50
#     # sleep(30)
#     print(f"Total Cost (USD): ${cb.total_cost}")

#   chain.batch([{ "description": purpose } for purpose in new_purposes[:100]])
#   print(f"[{i}] Cost: ${cb.total_cost} | Total Tokens: {cb.total_tokens}")
  # print(f"Total Cost (USD): ${cb.}")
