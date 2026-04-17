import json
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pickle
import os

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import MODEL_NAME, DATASET_PATH, EMBEDDINGS_PATH

model = SentenceTransformer(MODEL_NAME)


def load_dataset():
    df = pd.read_csv(DATASET_PATH)
    df["tags"] = df["tags"].apply(json.loads)
    return df


def build_embeddings(df):
    texts = []
    for _, row in df.iterrows():
        combined = f"{row['title']} {row['category']} {' '.join(row['tags'])} {row['description']}"
        texts.append(combined)

    embeddings = model.encode(texts, show_progress_bar=True)
    return embeddings


def save_embeddings(embeddings, df):
    os.makedirs("models", exist_ok=True)
    with open(EMBEDDINGS_PATH, "wb") as f:
        pickle.dump({"embeddings": embeddings, "ids": df["id"].tolist()}, f)
    print(f"Embeddings saved to {EMBEDDINGS_PATH}")


def load_embeddings():
    with open(EMBEDDINGS_PATH, "rb") as f:
        data = pickle.load(f)
    return data["embeddings"], data["ids"]


def get_embeddings(df):
    if os.path.exists(EMBEDDINGS_PATH):
        print("Loading embeddings from cache...")
        return load_embeddings()
    else:
        print("Building embeddings for the first time...")
        embeddings = build_embeddings(df)
        save_embeddings(embeddings, df)
        return embeddings, df["id"].tolist()


def extract_intent(query: str, df: pd.DataFrame):
    query_lower = query.lower()

    
    category_tags = {}
    for _, row in df.iterrows():
        cat = row["category"]
        if cat not in category_tags:
            category_tags[cat] = set()
        category_tags[cat].update(row["tags"])

  
    category_scores = {}
    matched_tags = []

    for category, tags in category_tags.items():
        score = 0
        for tag in tags:
            if tag in query_lower:
                score += 1
                matched_tags.append(tag)
        category_scores[category] = score

    best_category = max(category_scores, key=category_scores.get)

    
    if category_scores[best_category] == 0:
        best_category = "unknown"

    return {
        "category": best_category,
        "matched_tags": list(set(matched_tags)),
        "query": query
    }


def embed_query(query: str):
    return model.encode([query])[0]