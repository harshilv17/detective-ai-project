import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from loader import load_documents


# Load documents
documents = load_documents("data")

# Extract only text
texts = [doc["content"] for doc in documents]

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create embeddings
embeddings = model.encode(texts)

# Convert to float32 for FAISS
embeddings = np.array(embeddings).astype("float32")

# Build FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)


def search(query, k=1):
    query_embedding = model.encode([query]).astype("float32")
    distances, indices = index.search(query_embedding, k)

    results = [documents[i] for i in indices[0]]
    return results


if __name__ == "__main__":
    query = "What was found near the scene?"
    results = search(query)

    print("Top Match:")
    print(results[0])
