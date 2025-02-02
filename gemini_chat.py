import google.generativeai as genai
from config import GEMINI_API_KEY
from vector_store import retrieve_similar

## Setup Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Generate response using RAG
def generate_response(user_query):
    retrieved_docs = retrieve_similar(user_query)
    context = "\n".join(retrieved_docs)
    
    prompt = f"Context:\ n{context}\n\nUser Query: {user_query}\nResponse:"
    
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    
    return response

# Test example
if __name__ == "__main__":
    query = "Describe two major challenges faced by current AI systems."
    bot_response = generate_response(query)
    print("🤖 Chatbot Response:", bot_response)