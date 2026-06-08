import chromadb
import gradio as gr
from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

chroma_client = chromadb.PersistentClient(path="chroma_db")
collection = chroma_client.get_collection("reviews")


def ask(question):
    query_embedding = embedding_model.encode(question).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=1
    )

    docs = results["documents"][0]
    metas = results["metadatas"][0]

    answer = "Based on the retrieved student reviews:\n\n"

    sources = []

    for i, doc in enumerate(docs):
        answer += f"- {doc}\n\n"
        sources.append(metas[i]["source"])

    source_text = "\n".join(set(sources))

    return answer, source_text


with gr.Blocks() as demo:
    gr.Markdown("# The Unofficial Guide")

    question = gr.Textbox(label="Ask a question")
    answer = gr.Textbox(label="Answer", lines=10)
    sources = gr.Textbox(label="Sources", lines=4)

    button = gr.Button("Ask")

    button.click(
        ask,
        inputs=question,
        outputs=[answer, sources]
    )

demo.launch()