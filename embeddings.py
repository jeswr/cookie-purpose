from langchain.globals import set_llm_cache
from langchain.embeddings import CacheBackedEmbeddings
from langchain.storage import LocalFileStore
from langchain_community.cache import SQLiteCache
from langchain_openai import OpenAIEmbeddings, OpenAI, ChatOpenAI
import os

# Get the directory of the current module
module_dir = os.path.dirname(__file__)

set_llm_cache(SQLiteCache(database_path=os.path.join(module_dir, "./cache/llm.db")))

underlying_embeddings = OpenAIEmbeddings()
store = LocalFileStore(os.path.join(module_dir, "./cache/"))

embedder = CacheBackedEmbeddings.from_bytes_store(
    underlying_embeddings, store, namespace=underlying_embeddings.model, query_embedding_cache=True
)

model = ChatOpenAI(model="gpt-4o-mini-2024-07-18", temperature=0)
# model = OpenAI(model="gpt-4o")
