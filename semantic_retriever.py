from sentence_transformers import SentenceTransformer
import pickle

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("coffee_faiss.pkl", "rb") as f:
    index, docs = pickle.load(f)

def semantic_search(query, threshold=0.65):
    q_vec = model.encode([query])
    D, I = index.search(q_vec, 1)
    score = 1 / (1 + D[0][0])
    if score < threshold:
        return None
    return docs[I[0][0]]
