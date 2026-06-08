import os

docs_path = "docs"
documents = []

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


for file in os.listdir(docs_path):
    if file.endswith(".txt"):
        filepath = os.path.join(docs_path, file)

        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()

        chunks = chunk_text(text)

        for i, chunk in enumerate(chunks):
            documents.append({
                "source": file,
                "chunk_id": i,
                "text": chunk
            })


print("Total chunks:", len(documents))

for doc in documents:
    print("-----")
    print("Source:", doc["source"])
    print("Chunk:", doc["chunk_id"])
    print(doc["text"])