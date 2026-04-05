import streamlit as st
import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
import os

# --- PAGE SETUP ---
st.set_page_config(page_title="Steam AI Search", page_icon="🎮", layout="centered")
st.title("🎮 Steam AI Game Finder")
st.markdown("Search for games by **vibe, plot, or mechanics** instead of just keywords!")

# --- CACHING (Loads the AI once so it stays fast) ---
@st.cache_resource
def load_ai_model():
    # Gets the exact folder where search.py lives
    current_folder = os.path.dirname(os.path.abspath(__file__))
    
    # Points to the local steam_nlp_model directory in the same folder
    # Note: there's an extra nested folder!
    model_path = os.path.join(current_folder, 'steam_nlp_model', 'steam_nlp_model')
    
    print(f"Looking for AI files exactly here: {model_path}")
    return SentenceTransformer(model_path)

@st.cache_resource
def load_faiss():
    # Points to your local database!
    return faiss.read_index('steam_faiss_index.bin')

@st.cache_data
def load_dataset():
    # Points to your local CSV!
    return pd.read_csv('steam_ready_for_search.csv')

# Load everything into memory
with st.spinner("Loading AI Model and Database (this takes a few seconds)..."):
    model = load_ai_model()
    index = load_faiss()
    df = load_dataset()

# --- USER INTERFACE ---
query = st.text_input("What kind of game do you want to play?", placeholder="e.g. escaping a terrifying monster in space")
top_k = st.slider("Number of results to show", min_value=1, max_value=10, value=5)

# --- SEARCH ENGINE LOGIC ---
if st.button("Search") and query:
    with st.spinner(f"Searching 27,000+ games for '{query}'..."):
        
        # 1. Convert text to vector using your local model
        query_vector = model.encode([query], convert_to_numpy=True)
        faiss.normalize_L2(query_vector)
        
        # 2. Search local FAISS index
        scores, indices = index.search(query_vector, top_k)
        
        # 3. Display Results
        st.write("### Top Matches:")
        
        for i in range(top_k):
            game_idx = indices[0][i]
            score = scores[0][i]
            
            title = df.iloc[game_idx]['name']
            genre = df.iloc[game_idx]['genres']
            desc = df.iloc[game_idx]['short_description']
            
            # Create a visual card for each game
            with st.container():
                st.markdown(f"#### 🕹️ {title}")
                st.caption(f"**Match Score:** {score:.4f} | **Genres:** {genre}")
                st.write(desc)
                st.divider()