from langchain.globals import set_llm_cache
from langchain.embeddings import CacheBackedEmbeddings
from langchain.storage import LocalFileStore
from langchain.cache import SQLiteCache
from langchain_openai import OpenAIEmbeddings, OpenAI

set_llm_cache(SQLiteCache(database_path="./cache/llm.db"))

underlying_embeddings = OpenAIEmbeddings()
store = LocalFileStore("./cache/")

embedder = CacheBackedEmbeddings.from_bytes_store(
    underlying_embeddings, store, namespace=underlying_embeddings.model, query_embedding_cache=True
)

model = OpenAI(model="gpt-4o-mini-2024-07-18")
