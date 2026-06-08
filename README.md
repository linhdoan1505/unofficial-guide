# The Unofficial Guide

## Project Overview

This project is a Retrieval-Augmented Generation (RAG) system designed to answer student questions about courses and professors using real student review documents.

The system retrieves relevant text chunks from stored reviews and generates grounded responses with source attribution.

---

## Domain and Document Sources

Domain: University course and professor reviews.

Documents used:

- cs221_reviews.txt
- acct201_reviews.txt
- econ102_reviews.txt

These documents contain student-written opinions and experiences about courses and professors.

---

## Chunking Strategy and Reasoning

The documents were chunked by paragraph using blank lines as separators.

Reasoning:
- Student reviews are naturally short and paragraph-based.
- Keeping chunks small improves retrieval relevance.
- No overlap was used because the reviews are already concise.

Average chunk size:
- 1–3 paragraphs per chunk.

---

## Sample Chunks

### Chunk 1
Source: cs221_reviews.txt

> Dr. Park is genuinely very supportive and smart.

### Chunk 2
Source: cs221_reviews.txt

> Lab sessions are quite manageable. There is teamwork involved for the last two labs.

### Chunk 3
Source: acct201_reviews.txt

> Dr. Sadler explains concepts clearly but exams are tricky.

### Chunk 4
Source: econ102_reviews.txt

> He hosts amazing review sessions before exams and will buy you great pizza!

### Chunk 5
Source: econ102_reviews.txt

> Dr. Christensen is extremely kind and caring.

---

## Embedding Model Used

Embedding model:
`sentence-transformers/all-MiniLM-L6-v2`

Why this model:
- Lightweight
- Fast local inference
- Good semantic retrieval quality
- Easy to run on a laptop

Production tradeoffs:
For larger deployments, I would consider:
- retrieval accuracy
- latency
- GPU requirements
- embedding dimensionality
- API cost vs local hosting

Larger models may improve retrieval quality but increase cost and inference time.

---

## Retrieval Test Results

### Query 1
Question:
> Which professor hosts helpful review sessions?

Top retrieved chunk:
> He hosts amazing review sessions before exams and will buy you great pizza!

Why relevant:
This chunk directly discusses review sessions and identifies the professor.

---

### Query 2
Question:
> Which class has teamwork in labs?

Top retrieved chunk:
> Lab sessions are quite manageable. There is teamwork involved for the last two labs.

Why relevant:
The chunk directly references teamwork and labs.

---

### Query 3
Question:
> Which professor explains concepts clearly?

Top retrieved chunk:
> Dr. Sadler explains concepts clearly but exams are tricky.

---

## Grounded Generation Strategy

Grounded generation is enforced by:
- retrieving only relevant chunks from the vector database
- restricting the generated answer to retrieved context
- displaying source attribution with responses

The system does not answer using outside information.

---

## Example Responses

### Example 1

Question:
> Which professor buys pizza?

Response:
> Dr. Christensen hosts review sessions before exams and buys pizza.

Source:
econ102_reviews.txt

---

### Example 2

Question:
> Which course includes teamwork?

Response:
> CS221 includes teamwork in the final labs.

Source:
cs221_reviews.txt

---

### Out-of-Scope Query

Question:
> What is the weather today?

Response:
> I can only answer questions related to the uploaded student review documents.

---

## Query Interface

Input:
- User question text

Output:
- Generated response
- Source document names

### Sample Interaction

Question:
> Which professor is supportive?

Response:
> Dr. Park is supportive and smart.

Source:
cs221_reviews.txt

---

## Evaluation Report

| Question | Expected Answer | System Response | Accurate? |
|---|---|---|---|
| Which professor buys pizza? | Dr. Christensen | Correctly identified Dr. Christensen | Yes |
| Which course has teamwork? | CS221 | Correctly identified CS221 labs | Yes |
| Which professor explains concepts clearly? | Dr. Sadler | Correctly identified Dr. Sadler | Yes |
| Which professor is caring? | Dr. Christensen | Correctly identified Dr. Christensen | Yes |
| Which class has manageable labs? | CS221 | Correctly identified CS221 | Yes |

---

## Failure Case

Failure:
The system sometimes returns overly broad answers because retrieval similarity scores are imperfect.

Reason:
Small datasets can cause unrelated chunks to appear in top results.

Potential improvement:
- better chunking
- top-k filtering
- reranking models

---

## Spec Reflection

One way the spec helped:
- It provided a clear structure for building a retrieval pipeline.

One way implementation diverged:
- I used lightweight local embeddings instead of a larger cloud model because of API quota limitations.

---

## AI Usage

### Instance 1
I used AI assistance to help structure the embedding and retrieval pipeline.

I revised:
- chunking logic
- retrieval formatting
- source attribution display

### Instance 2
I used AI assistance to debug Python environment and dependency issues.

I revised:
- package installation steps
- Gradio interface setup
- retrieval testing workflow

---

## Demo Video

The demo video includes:
- 3 successful queries
