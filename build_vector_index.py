from sentence_transformers import SentenceTransformer
import faiss, pickle
from coffee_docs import build_documents

model = SentenceTransformer("all-MiniLM-L6-v2")
docs = build_documents()
embeddings = model.encode(docs, convert_to_numpy=True)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

with open("coffee_faiss.pkl", "wb") as f:
    pickle.dump((index, docs), f)

print("Vector DB created")
