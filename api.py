from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
import os

app = FastAPI(title="Steam AI Search API")

# Setup CORS for the React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # For development, allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global variables for models
model = None
index = None
df = None

@app.on_event("startup")
async def load_models():
    global model, index, df
    current_folder = os.path.dirname(os.path.abspath(__file__))
    
    print("Loading AI Model...")
    model_path = os.path.join(current_folder, 'steam_nlp_model', 'steam_nlp_model')
    model = SentenceTransformer(model_path)
    
    print("Loading FAISS Index...")
    index_path = os.path.join(current_folder, 'steam_faiss_index.bin')
    index = faiss.read_index(index_path)
    
    print("Loading Dataset...")
    csv_path = os.path.join(current_folder, 'steam_ready_for_search.csv')
    df = pd.read_csv(csv_path)
    
    print("All models and data loaded successfully!")

@app.get("/search")
async def search(q: str = Query(..., description="The search query"), top_k: int = Query(5, description="Number of results")):
    """
    Search for games based on semantic meaning of the query.
    """
    if not q.strip():
        return {"results": []}

    # 1. Convert text to vector
    query_vector = model.encode([q], convert_to_numpy=True)
    faiss.normalize_L2(query_vector)
    
    # 2. Search local FAISS index
    scores, indices = index.search(query_vector, top_k)
    
    # 3. Format Results
    results = []
    for i in range(top_k):
        game_idx = indices[0][i]
        score = float(scores[0][i])
        
        # Get raw data (cleaning up any nan/null values just in case)
        appid = int(df.iloc[game_idx]['appid'])
        title = str(df.iloc[game_idx]['name'])
        genres = str(df.iloc[game_idx]['genres'])
        desc = str(df.iloc[game_idx]['short_description'])
        
        results.append({
            "appid": appid,
            "title": title,
            "genres": genres,
            "description": desc,
            "score": score
        })
        
    return {"results": results}
