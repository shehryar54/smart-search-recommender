"""
Smart Search & Recommendation API
----------------------------------
A FastAPI-based backend that understands natural language queries
and recommends the most relevant freelancers using NLP and semantic search.

Endpoints:
    POST /analyze               - Extract intent from query
    GET  /recommend             - Get ranked freelancer recommendations
    POST /simulate-interaction  - Log user interactions
"""


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.nlp import load_dataset, get_embeddings, extract_intent
from app.recommender import get_recommendations
import json

app = FastAPI(
    title="Smart Search & Recommendation API",
    description="AI-powered freelancer recommendation system",
    version="1.0.0"
)

df = load_dataset()
freelancer_embeddings, ids = get_embeddings(df)

class QueryRequest(BaseModel):
    query: str

class InteractionRequest(BaseModel):
    user_id: str
    freelancer_id: int
    action: str  # "view", "click", "hire"

@app.get("/")
def root():
    """Health check endpoint."""
    return {"status": "running", "message": "Smart Search API is live"}


@app.post("/analyze")
def analyze(request: QueryRequest):
    """
    Extract intent from a natural language query.
    Returns detected category and matched tags.
    """
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    intent = extract_intent(request.query, df)
    return {
        "query": request.query,
        "category": intent["category"],
        "matched_tags": intent["matched_tags"]
    }


@app.get("/recommend")
def recommend(query: str, top_n: int = 5):
    """
    Get top N recommended freelancers for a natural language query.
    Returns ranked results with scores and explanations.
    """
    if not query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    if top_n < 1 or top_n > 20:
        raise HTTPException(status_code=400, detail="top_n must be between 1 and 20")

    results = get_recommendations(query, top_n)
    return results


@app.post("/simulate-interaction")
def simulate_interaction(request: InteractionRequest):
    """
    Log a user interaction with a freelancer.
    Can be used for future personalization improvements.
    """
    valid_actions = ["view", "click", "hire"]
    if request.action not in valid_actions:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid action. Must be one of: {valid_actions}"
        )

    # for now just log and return — future: save to database
    print(f"Interaction logged: user={request.user_id}, freelancer={request.freelancer_id}, action={request.action}")

    return {
        "status": "logged",
        "user_id": request.user_id,
        "freelancer_id": request.freelancer_id,
        "action": request.action
    }