# 🎌 AI Anime Recommender

An intelligent anime recommendation system powered by RAG (Retrieval Augmented Generation) and vector similarity search. Get personalized anime suggestions based on your preferences using AI.

## 🌟 Features

- **AI-Powered Recommendations**: Uses GROQ LLM for intelligent, context-aware suggestions
- **Vector Search**: ChromaDB-based semantic search for finding similar anime
- **Interactive UI**: Clean Streamlit interface for easy interaction
- **Personalized Results**: Tailored recommendations based on your mood, genre preferences, and viewing history

## 🛠️ Tech Stack

- **LLM**: GROQ API (GPT-OSS:120b model)
- **Vector Database**: ChromaDB
- **Embeddings**: Sentence Transformers
- **Framework**: LangChain
- **Frontend**: Streamlit
- **Language**: Python 3.13+

## 📁 Project Structure

```
AI Anime Recommender/
├── app/                    # Streamlit application
├── src/                    # Core modules
│   ├── data_loader.py     # Data processing
│   ├── vector_store.py    # Vector database management
│   ├── recommender.py     # Recommendation engine
│   └── prompt_template.py # LLM prompts
├── pipeline/              # Data pipeline
│   ├── build_pipeline.py  # One-time setup
│   └── pipeline.py        # Runtime operations
├── data/                  # Anime dataset
├── config/                # Configuration files
└── utils/                 # Logging & error handling
```

## 🚀 Getting Started

### Prerequisites

- Python 3.13 or higher
- GROQ API key 

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/deep1305/Anime-Recommender-System-LLMOPS.git
   cd "AI Anime Recommender"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Build the data pipeline** (one-time setup)
   ```bash
   python pipeline/build_pipeline.py
   ```
   This processes the anime data and creates vector embeddings.

5. **Run the application**
   ```bash
   streamlit run app/app.py
   ```

6. **Open your browser** to `http://localhost:8501`

## 💡 Usage

Simply enter your anime preferences in natural language:

- *"Light-hearted anime with school settings"*
- *"Dark fantasy with complex characters"*
- *"Action-packed shounen with friendship themes"*
- *"Romantic comedy set in modern Japan"*

The AI will analyze your query and recommend relevant anime with detailed explanations.

## 🐳 Docker Deployment

Build and run with Docker:

```bash
# Build the image
docker build -t anime-recommender .

# Run the container
docker run -p 8501:8501 --env-file .env anime-recommender
```

Access at `http://localhost:8501`

## ☸️ Kubernetes Deployment

Deploy to Kubernetes cluster:

```bash
# Create secrets
kubectl create secret generic llmops-secrets \
  --from-literal=GROQ_API_KEY=your_api_key

# Apply manifests
kubectl apply -f llmops-k8s.yaml

# Get external IP
kubectl get service llmops-service
```

## 📊 How It Works

1. **Data Processing**: Anime data (titles, genres, synopses) is cleaned and formatted
2. **Embedding Generation**: Text is converted to vector embeddings using Sentence Transformers
3. **Vector Storage**: Embeddings are stored in ChromaDB for fast similarity search
4. **Query Processing**: User input is embedded and matched against the database
5. **LLM Generation**: GROQ generates personalized recommendations based on retrieved context


## 🙏 Acknowledgments

- Anime data sourced from public datasets
- Built with LangChain and ChromaDB
- Powered by GROQ's fast LLM inference

---

**Made with ❤️ for anime fans**

