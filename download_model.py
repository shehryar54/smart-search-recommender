from huggingface_hub import snapshot_download

print("Downloading model... this may take a few minutes")
snapshot_download('sentence-transformers/all-MiniLM-L6-v2')
print("Model downloaded successfully!")