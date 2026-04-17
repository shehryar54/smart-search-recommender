# AI-Powered Smart Search & Recommendation System

A backend system that understands natural language requests and recommends
the most relevant freelancers/services using NLP and semantic search.

## How it works

User types: "I need a flutter developer for mobile app"
↓
System extracts intent: category=mobile development, tags=[flutter]
↓
Semantic search across 50 freelancer profiles
↓
Hybrid ranking: text similarity (70%) + rating (30%)
↓
Returns top 5 results with explanation

## Features
- Natural language query understanding
- Semantic similarity search using sentence embeddings
- Hybrid ranking — relevance + rating
- "Why recommended" explanation for each result
- Input validation and edge case handling
- Clean REST API with auto-generated documentation

## Tech Stack
- Python 3.14 + FastAPI
- Sentence Transformers (all-MiniLM-L6-v2)
- Scikit-learn, Pandas, NumPy
- Flutter (frontend — separate repo)

## Project Structure

smart_search/
├── app/
│   ├── main.py          # FastAPI routes
│   ├── nlp.py           # Intent extraction + embeddings
│   └── recommender.py   # Ranking + recommendation logic
├── data/
│   ├── seed_data.py     # Dataset generator
│   └── freelancers.csv  # 50 freelancer profiles
├── config.py            # Central settings
├── requirements.txt
└── README.md

## Setup

```bash
git clone https://github.com/shehryar54/smart-search-recommender.git
cd smart-search-recommender

python -m venv venv
venv\Scripts\activate  
source venv/bin/activate  

pip install -r requirements.txt

python data/seed_data.py

uvicorn app.main:app --reload
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/analyze` | Extract intent from query |
| GET | `/recommend` | Get ranked recommendations |
| POST | `/simulate-interaction` | Log user interaction |

## Example

**Request:**
```json
POST /analyze
{
  "query": "I need a video editor for instagram reels"
}
```

**Response:**
```json
{
  "query": "I need a video editor for instagram reels",
  "category": "video editing",
  "matched_tags": ["reels", "instagram"]
}
```

## API Documentation
Run the server and visit `http://127.0.0.1:8000/docs` for interactive documentation.

## Project Status
✅ Complete — built as a portfolio project