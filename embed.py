from sentence_transformers import SentenceTransformer
import chromadb
import os

# load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# create/load chroma database
client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection("reviews")


# chunking function
def chunk_text(text, chunk_size=500, overlap=50):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


docs_path = "docs"

id_counter = 0

# load documents
for file in os.listdir(docs_path):

    if file.endswith(".txt"):

        filepath = os.path.join(docs_path, file)

        with open(filepath, "r", encoding="utf-8") as f:

            text = f.read()

        chunks = chunk_text(text)

        for i, chunk in enumerate(chunks):

            embedding = model.encode(chunk).tolist()

            collection.add(
                ids=[str(id_counter)],
                embeddings=[embedding],
                documents=[chunk],
                metadatas=[{
                    "source": file,
                    "chunk_id": i
                }]
            )

            print(f"Added chunk {id_counter}")

            id_counter += 1


print("Embedding complete!")