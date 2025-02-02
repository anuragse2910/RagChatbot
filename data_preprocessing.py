import os
import nltk
from nltk.tokenize import sent_tokenize
from sentence_transformers import SentenceTransformer

if not os.path.exists(nltk.data.find("tokenizers/punkt")):
    nltk.download("punkt")

# Load Corpus
def load_corpus(file_path="data/corpus.txt"):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

# Split Text into Chunks
def chunk_text(text, chunk_size=200):
    sentences = sent_tokenize(text)
    chunks = [" ".join(sentences[i : i + chunk_size]) for i in range(0, len(sentences), chunk_size)]
    return chunks

# Convert to Embeddings
def embed_text(chunks):
    model = SentenceTransformer("all-MiniLM-L6-v2")  # Efficient embedding model
    return model.encode(chunks)

if __name__ == "__main__":
    text = load_corpus()
    chunks = chunk_text(text)
    embeddings = embed_text(chunks)
    
    print(f"Total Chunks: {len(chunks)}")
    print(f"First Chunk: {chunks[0]}")