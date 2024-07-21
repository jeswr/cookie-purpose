from dotenv import load_dotenv
load_dotenv()

from purposes import purposes
from embeddings import embedder
from langchain_community.vectorstores import Qdrant
import asyncio
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
import faiss
import os
from sklearn.cluster import DBSCAN
import numpy as np


async def main():
  # print(faiss)
  embeddings_array=np.array(embedder.embed_documents(purposes[:100])).astype('float32')
  # print(len(embeddings_array))

  # Perform DBSCAN clustering
  dbscan = DBSCAN(eps=0.5, min_samples=2, metric='euclidean')
  cluster_assignments = dbscan.fit_predict(embeddings_array)
  print(cluster_assignments)

  # Get unique cluster labels
  # unique_labels = set(cluster_assignments)


  # db = FAISS.from_texts(purposes[:10], embedder)
  # db.
  # db = FAISS.from_documents(docs, embeddings)
  # print(db.index.ntotal)
  # print(purposes[:10])
  # db = await Qdrant.afrom_texts(purposes[:10], embedder, url="https://d1ab2bda-74c4-44cd-a5c5-838effb85b40.us-east4-0.gcp.cloud.qdrant.io", port=6333, api_key=os.getenv("QDRANT_API_KEY"))
  # db.
  # print(db.)
  # db.amax_marginal_relevance_search_by_vector

asyncio.run(main())
