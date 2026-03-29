# AI-Powered Smart Search & Recommendation System

A backend system that understands natural language requests and recommends
the most relevant freelancers/services using NLP and semantic search.

## Features
- Natural language query understanding (intent + tag extraction)
- Semantic similarity search using sentence embeddings
- Hybrid ranking (text similarity + rating score)
- "Why recommended" explanation for each result
- Clean REST API built with FastAPI

## Tech Stack
- Python 3.14 + FastAPI
- Sentence Transformers (all-MiniLM-L6-v2)
- Scikit-learn, Pandas, NumPy
- Flutter (frontend — separate repo)

## Project Status
🚧 In active development

## Setup
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/analyze` | Extract intent from query |
| GET | `/recommend` | Get ranked recommendations |
| POST | `/simulate-interaction` | Log user interaction |