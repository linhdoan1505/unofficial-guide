from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_collection("reviews")


def search(query):
    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    return results


question = "Which professor gives helpful review sessions?"

results = search(question)

print("QUESTION:", question)

for i in range(len(results["documents"][0])):
    print("-----")
    print("Source:", results["metadatas"][0][i]["source"])
    print("Chunk:", results["metadatas"][0][i]["chunk_id"])
    print("Distance:", results["distances"][0][i])
    print(results["documents"][0][i])