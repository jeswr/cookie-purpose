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
from sklearn.neighbors import NearestNeighbors
import numpy as np
import matplotlib.pyplot as plt
from requestDebugger import debug_requests_on
debug_requests_on()

async def main():
  embeddings=np.array(embedder.embed_documents(purposes[:100])).astype('float32')

  k = 4  # Typically set k to min_samples
  neighbors = NearestNeighbors(n_neighbors=k)
  neighbors_fit = neighbors.fit(embeddings)
  distances, indices = neighbors_fit.kneighbors(embeddings)

  # Sort the distances (k-th nearest distances)
  distances = np.sort(distances[:, k-1], axis=0)

  plt.plot(distances)
  plt.xlabel('Data Points sorted by distance')
  plt.ylabel(f'{k}-th Nearest Neighbor Distance')
  plt.title('k-distance Graph')
  plt.show()

  exit()

  
  # print(len(embeddings_array))

  # Perform DBSCAN clustering
  dbscan = DBSCAN(eps=0.5, min_samples=2, metric='euclidean')
  cluster_assignments = dbscan.fit_predict(embeddings)
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
