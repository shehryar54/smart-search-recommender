import json
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from app.nlp import load_dataset, get_embeddings, embed_query, extract_intent


def validate_query(query: str) -> bool:
    
    query = query.strip()
    if len(query) < 3:
        return False
    if not any(c.isalpha() for c in query):
        return False
    return True



def compute_scores(query_embedding, freelancer_embeddings, df):
    similarities = cosine_similarity(
        [query_embedding], freelancer_embeddings
    )[0]

    max_rating = df["rating"].max()
    normalized_ratings = df["rating"] / max_rating

    final_scores = (similarities * 0.7) + (normalized_ratings * 0.3)

    return similarities, final_scores

def build_explanation(row, similarity_score, matched_tags):
    explanation_parts = []

    if matched_tags:
        common_tags = [tag for tag in matched_tags if tag in row["tags"]]
        if common_tags:
            explanation_parts.append(f"matched tags: {', '.join(common_tags)}")

    explanation_parts.append(f"relevance score: {round(similarity_score, 2)}")
    explanation_parts.append(f"rating: {row['rating']}/5.0")

    return " | ".join(explanation_parts)

def get_recommendations(query: str, top_n: int = 5):
    
    if not validate_query(query):
        return {
            "query": query,
            "intent": {"category": "unknown", "matched_tags": []},
            "results": [],
            "message": "Query too short or invalid. Please describe what you need."
        }

    df = load_dataset()
    freelancer_embeddings, ids = get_embeddings(df)

    intent = extract_intent(query, df)

    query_embedding = embed_query(query)

    similarities, final_scores = compute_scores(
        query_embedding, freelancer_embeddings, df
    )

    df["similarity_score"] = similarities
    df["final_score"] = final_scores

    top_results = df.nlargest(top_n, "final_score").copy()

    results = []
    for _, row in top_results.iterrows():
        results.append({
            "id": row["id"],
            "title": row["title"],
            "category": row["category"],
            "tags": row["tags"],
            "rating": row["rating"],
            "similarity_score": round(float(row["similarity_score"]), 3),
            "final_score": round(float(row["final_score"]), 3),
            "explanation": build_explanation(
                row,
                float(row["similarity_score"]),
                intent["matched_tags"]
            )
        })

    return {
        "query": query,
        "intent": intent,
        "results": results
    }