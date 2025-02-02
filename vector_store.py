import faiss
import numpy as np
from data_preprocessing import embed_text, chunk_text, load_corpus

# Load and process corpus
text = load_corpus()
chunks = chunk_text(text)
embeddings = embed_text(chunks)

# Convert embeddings to numpy array
embedding_dim = embeddings.shape[1]  # Get vector dimension
index = faiss.IndexFlatL2(embedding_dim)  # L2 distance index
index.add(np.array(embeddings))  # Add vectors to FAISS index

# # Save FAISS index
# faiss.write_index(index, "embeddings/faiss_index.bin")

# print(f"✅ FAISS index created with {len(chunks)} documents!")


def retrieve_similar(query, top_k=2):
    query_embedding = embed_text([query])  # Convert query to embedding
    distances, indices = index.search(np.array(query_embedding), top_k)  # Search FAISS index
    
    results = [chunks[i] for i in indices[0]]  # Fetch corresponding text chunks
    return results

# # Example retrieval test
# if __name__ == "__main__":
#     query = "Describe two major challenges faced by current AI systems."
#     results = retrieve_similar(query)
#     print("🔍 Retrieved Documents:", results)
