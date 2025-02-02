# RAG Chatbot

## Overview
This project is a Retrieval-Augmented Generation (RAG) chatbot that leverages information retrieval and generative AI to provide accurate and context-aware responses. The chatbot retrieves relevant documents from a knowledge base and uses a language model to generate responses based on both retrieved information and the conversation context.

## Features
- **Hybrid AI Approach**: Combines retrieval-based and generative AI techniques.
- **Contextual Understanding**: Maintains conversation context for coherent interactions.
- **Efficient Information Retrieval**: Fetches relevant data from a pre-indexed knowledge base.
- **Customizable Knowledge Base**: Supports updates and expansion.
- **Scalability**: Optimized for large-scale applications.

## Installation
### Prerequisites
- Python (>=3.8)
- Pip
- Virtual environment (optional but recommended)

### Setting Up the Environment
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/rag-chatbot.git
   cd rag-chatbot
   ```
2. Set up a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install dependencies from the provided `requirements.txt`:
   ```sh
   pip install -r requirements.txt
   ```

### Running the Project
1. Ensure all dependencies are installed.
2. Start the chatbot service:
   ```sh
   python app.py
   ```
3. Interact via the provided API or frontend interface.

## Configuration
- **Knowledge Base**: Add documents to `data/` and run preprocessing scripts.
- **Model Selection**: Modify `config.py` to switch between different language models.
- **API Integration**: Configure endpoints in `app.py` for external service integration.

## File Structure
```
rag-chatbot/
├── data/                       # Corpus files for retrieval
├── embeddings/                 # Stored vector embeddings
├── app.py                      # Main application script
├── gemini_chat.py              # Gemini model-based chatbot script
├── data_preprocessing.py       # Preprocessing script for cleaning and tokenizing data
├── config.py                   # Configuration settings
├── vectore_store.py            # Script to manage vector database operations
├── mysql_connection.py         # Database connection and query handling script
├── requirements.txt            # Dependencies for setting up the project
└── README.md                   # Project documentation
```

## License
This project is licensed under the MIT License.

## 👨‍💻 Author
👤 Anurag  
📌 [GitHub](https://github.com/anuragse2910) | 📧 [anuragselote12@gmail.com](mailto:anuragselote12@gmail.com)
