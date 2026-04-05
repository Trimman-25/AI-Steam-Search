🎮 AI-Powered Semantic Steam Search
📖 Project Overview
Traditional search engines rely on Keyword Matching—if you don't type the exact word, you don't find the result. This project transcends that limitation by implementing Semantic Search.

By leveraging Deep Learning, this application understands the intent and context behind a search. Whether you're looking for a "vibe" (e.g., cozy, melancholic, adrenaline-pumping) or a specific plot hook (e.g., betrayal in a high-fantasy setting), the AI identifies the most relevant games from a library of 27,000+ titles even if your search terms aren't in the description.

🧠 How the AI Works (The Deep Dive)
1. NLP & Sentence Embeddings
At the core of the project is Sentence-BERT (SBERT), specifically the all-MiniLM-L6-v2 transformer model.

The Process: The model converts raw English text into a 384-dimensional vector (a long list of numbers).

The Concept: Think of this as a mathematical "fingerprint" of a sentence's meaning. Similar concepts (like "terrifying" and "spooky") are mapped to coordinates that are physically close to each other in this 384-dimensional space.

2. High-Performance Vector Retrieval (FAISS)
Searching through 27,000 vectors one-by-one is slow. To make this instant, we use FAISS (Facebook AI Similarity Search).

Indexing: FAISS organizes the game vectors into a specialized structure that allows for "Nearest Neighbor" lookups in microseconds.

The Scoring System: We use Cosine Similarity. The "Match Score" you see in the app represents the cosine of the angle between your query vector and the game's vector.

1.00 means the vectors point in the exact same direction (perfect match).

Higher scores indicate a stronger conceptual overlap.

🛠️ Tech Stack
Backend (The Intelligence)
FastAPI: A modern, high-performance Python web framework used to build the Search API.

Sentence-Transformers: Used to load the PyTorch-based NLP model.

FAISS (CPU): Used as our vector database for high-speed similarity searches.

Pandas: Handles the metadata (titles, genres, IDs) from the Steam dataset.

Frontend (The Experience)
React (Vite): A fast, component-based UI library.

Vanilla CSS: Custom-engineered for a Glassmorphism aesthetic, featuring:

backdrop-filter: blur() for frosted-glass effects.

CSS variables for dynamic neon-glow accents.

Responsive Grid Layouts for game discovery.

Lucide-React: For modern, lightweight iconography.

📊 The Dataset
The project utilizes a comprehensive Steam Games Dataset containing metadata for approximately 27,000 games.

Data Used: We specifically trained the model on the detailed_description column to capture the full narrative depth of every game.

Dynamic Content: We use the appid from the dataset to fetch real-time assets from Steam’s Content Delivery Network (CDN), ensuring the UI always displays official high-quality game banners.

🚀 Impact: Why this helps?
Discovery: Helps users find "hidden gems" they wouldn't have found using standard tags.

Accessibility: Allows users to describe games in natural language (e.g., "that game with the talking cat in a city") instead of memorizing titles.

Speed: Demonstrates how AI can turn a massive, unstructured text database into an instantly searchable tool without the need for manual tagging.
