import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATASET_PATH = os.path.join(BASE_DIR, "data", "freelancers.csv")
EMBEDDINGS_PATH = os.path.join(BASE_DIR, "models", "embeddings.pkl")

MODEL_NAME = "all-MiniLM-L6-v2"

DEFAULT_TOP_N = 5
MAX_TOP_N = 20
SIMILARITY_WEIGHT = 0.7
RATING_WEIGHT = 0.3