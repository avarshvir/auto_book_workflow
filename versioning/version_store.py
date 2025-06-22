import chromadb
from datetime import datetime

client = chromadb.Client()
collection = client.get_or_create_collection(name="book_versions")

def save_version(text, tag="final"):
    ver_id = f"{tag}_{datetime.now().isoformat()}"
    collection.add(
        documents=[text],
        ids=[ver_id]
    )
    print(f"Version saved as: {ver_id}")

def search_version(query_text):
    results = collection.query(
        query_texts=[query_text],
        n_results=1
    )
    if results["documents"]:
        return results["documents"][0][0]
    return "No similar version found."
