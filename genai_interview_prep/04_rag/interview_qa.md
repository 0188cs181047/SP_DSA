# RAG — Retrieval-Augmented Generation

## Overview

RAG grounds an LLM's answer in text retrieved from your own data, instead of relying only on what the model memorized during training. It's the pattern that turns a general-purpose LLM into something that can answer questions about private, current, or simply too-large-to-fit-in-context documents.

## Data Flow Diagram — Offline + Runtime Pipeline

```mermaid
flowchart TD
    subgraph Offline["Offline — Ingestion (runs once / on a schedule)"]
        D1[Documents] --> C1[Chunk] --> E1[Embed] --> VDB[("Vector DB")]
    end
    subgraph Runtime["Runtime — Every user query"]
        Q[User Query] --> QE[Embed Query]
        QE -->|search| VDB
        VDB --> RC[Retrieved Chunks]
        Q --> AP["Augmented Prompt<br/>(context + query)"]
        RC --> AP
        AP --> LLM[LLM]
        LLM --> ANS[Grounded Answer]
    end
```

Ingestion builds the index once; the runtime lane re-uses it on every query — retrieval happens before the LLM ever sees the question.

## Interview Q&A

### Easy — Screening Round

**E1. What problem does RAG actually solve?**
LLMs only "know" what was in their training data plus whatever fits in the current context window. RAG lets a model answer questions about private, current, or very large document sets — without retraining — by fetching the relevant text and handing it to the model as context at answer time.

**E2. Walk through the RAG pipeline end-to-end.**
Offline: split documents into chunks, embed each chunk, store the vectors plus metadata in a vector database. At query time: embed the user's question, run an ANN search to pull the top-K most relevant chunks, build a prompt containing those chunks plus the original question, send it to the LLM, and return its answer.

**E3. What's the difference between "context" in RAG and the model's "context window"?**
In **RAG (Retrieval-Augmented Generation)**, **context** is the relevant information retrieved from the database and sent to the model along with the user's question.

The **context window** is the maximum amount of information the model can process in a single request. It must accommodate the system prompt, retrieved information, conversation history, the user's question, and the model's generated response.

### Example

Suppose a model has a context window of **8,000 tokens**. The prompt, conversation history, and retrieved chunks must fit within the available token budget, while leaving room for the model's answer.

### In simple words

- **RAG context:** The information selected and provided to the model for the current question.
- **Context window:** The model's overall token capacity for a request, including input and output.

### Important point

Retrieving too much information can exceed the model's context window and cause errors or force information to be left out. To avoid this, retrieve the most relevant chunks and check that the full request fits within the model's token limit.
"""


**E4. Does RAG require fine-tuning the LLM?**
No. **RAG does not require fine-tuning the LLM.** One of the main advantages of RAG is that it can work with an existing, pre-trained language model without changing the model's weights.

In a typical RAG workflow, the system retrieves relevant information from a knowledge source, such as documents or a vector database, and adds that information to the prompt along with the user's question. The LLM then uses the provided context to generate its answer.

Fine-tuning can be added later if there is a specific need, such as adapting the model to a particular response style, output format, or specialized task. However, fine-tuning is an optional enhancement, not a requirement for RAG.

**Key difference:**
- **RAG** provides the model with relevant external information at query time.
- **Fine-tuning** updates the model's weights using training examples to influence how it responds or performs a task.

**Example:** A company can build a chatbot that answers questions using internal policy documents by retrieving relevant passages and passing them to an existing LLM. This can be done without fine-tuning the model.
"""

**E5. What is a "chunk," and why split documents into chunks instead of embedding each whole document?**
A **chunk** is a small part of a document, such as a paragraph or a few sentences. Each chunk is converted into an embedding and stored in a vector database.


### E5. What is a Chunk, and Why Do We Split Documents into Chunks?

A **chunk** is a small part of a document, such as a paragraph or a few sentences. Each chunk is converted into an embedding and stored in a vector database.

**Why do we split documents into chunks?**

- **Better search:** Helps retrieve information relevant to the user's question.
- **Higher accuracy:** Reduces irrelevant information in the retrieved results.
- **Efficient retrieval:** Retrieves only the required part instead of the entire document.

**Example:**

Suppose a PDF contains 50 pages covering pricing, company policies, and legal information. If a user asks about pricing, chunking helps the RAG system retrieve only the relevant pricing section instead of the entire PDF.

**In short:** Chunking improves the relevance and efficiency of information retrieval in RAG systems.



### E6. What Is an Embedding, and How Is It Better Than Keyword Matching?

An **embedding** is a list of numbers (a vector) that represents the meaning of text. Texts with similar meanings have embeddings that are close to each other in the vector space.

**Why do we use embeddings?**

- **Semantic search:** Finds information based on meaning, not just exact words.
- **Better results:** Can find relevant information even when different words are used.
- **Improved retrieval:** Helps RAG systems retrieve relevant document chunks for a user's question.

**Example:**

If a user searches for "cheap flights," an embedding-based search can find a document containing "budget airfare" because both phrases have similar meanings.

Keyword matching might miss this result because the exact words are different.

**In short:** Embeddings help search systems understand the meaning of text rather than matching only exact keywords.


**E7. What is a vector database, and why not just store embeddings in a regular SQL table?**
A vector database stores embeddings alongside metadata and is built specifically to answer "which stored vectors are closest to this query vector" quickly, using approximate nearest-neighbor (ANN) indexes. A regular SQL database has no efficient way to do that similarity search at scale — you'd be stuck computing distance to every single row, which doesn't scale past a small table.

**E8. What does "top-K" mean when people talk about retrieval?**
K is simply how many of the highest-scoring chunks you pull back and hand to the LLM — top-5, top-10, whatever you configure. Too small a K risks missing a relevant chunk that scored just outside the cutoff; too large a K pads the prompt with marginally relevant text, burning context-window budget and risking the Lost-in-the-Middle problem.

**E9. In the RAG pipeline, which part does retrieval and which part does generation — and can you swap either piece independently?**
The embedding model plus the vector database handle retrieval — finding relevant chunks; the LLM handles generation — turning those chunks plus the question into a final answer. They're decoupled by design: you can swap the embedding model, the vector database, or the LLM independently, as long as whatever produced the stored vectors also produces the query vector — mixing embedding models breaks similarity search, since their vector spaces aren't compatible with each other.

### Medium — Technical Round


### M1. How Does RAG Reduce Hallucination?

**RAG (Retrieval-Augmented Generation)** reduces hallucination by providing the LLM with relevant information retrieved from trusted documents before generating an answer.

**How does it work?**

1. **Retrieve:** Finds relevant information from a document or vector database.
2. **Augment:** Adds the retrieved information to the LLM's prompt as context.
3. **Generate:** The LLM uses the provided context to generate an answer based on the available information.

**Example:**

Suppose a company document states that its leave policy allows 20 days of annual leave. If a user asks about the leave policy, RAG retrieves the relevant section and provides it to the LLM to generate an answer.

Without RAG, the LLM might generate an incorrect answer based on its existing knowledge.

**Important:** RAG reduces hallucination but does not eliminate it completely. The LLM may misinterpret the retrieved information, ignore the context, or generate unsupported answers.

**In short:** RAG improves answer accuracy by grounding the LLM's responses in relevant source information.



### M2. What Is the Difference Between Naive RAG and Advanced RAG?

**Naive RAG** follows a simple process: retrieve relevant document chunks and provide them to the LLM to generate an answer.

**Advanced RAG** improves this process by adding techniques to retrieve more relevant information and generate more accurate answers.

**Key Differences:**

| Naive RAG | Advanced RAG |
|---|---|
| Uses a simple retrieval process. | Uses improved retrieval techniques. |
| Searches using the original user query. | Can rewrite or expand the query. |
| Typically uses vector search. | Can combine keyword search and vector search (hybrid search). |
| May retrieve irrelevant chunks. | Can use re-ranking to select the most relevant chunks. |
| Uses a straightforward retrieval and generation flow. | Can use multi-step retrieval and self-checking mechanisms. |

**Example:**

Suppose a user asks, "What is the company's leave policy?"

- **Naive RAG:** Retrieves document chunks based on the original query and generates an answer.
- **Advanced RAG:** Can rewrite the query, combine keyword and semantic search, re-rank the retrieved chunks, and use the most relevant information to generate an answer.

**In short:** Naive RAG uses a basic retrieval pipeline, whereas Advanced RAG adds techniques to improve retrieval quality and answer accuracy.



### M3. What Is Hybrid Search?

**Hybrid search** combines keyword search and vector search to find the most relevant information from documents.

It uses two search methods:

1. **Keyword Search (BM25):** Finds documents containing exact words or terms.
2. **Vector Search:** Finds documents based on the meaning and similarity of the text using embeddings.

The results from both methods are combined or re-ranked to improve search accuracy.

**Why do we use hybrid search?**

- Finds exact keywords, product codes, names, and acronyms.
- Retrieves information based on meaning, even when the wording is different.
- Improves the relevance of search results.

**Example:**

Suppose a user searches for `Python FastAPI`.

- **Keyword Search:** Finds documents containing the exact terms `Python` and `FastAPI`.
- **Vector Search:** May also find documents discussing Python API development using similar wording.
- **Hybrid Search:** Combines both results to find relevant information more effectively.

**In short:** Hybrid search combines keyword matching and semantic search to improve information retrieval in RAG systems.

**M4. How do you evaluate a RAG system?**
Two layers: retrieval metrics (precision/recall@K, MRR — did we fetch the right chunks?) and generation metrics (faithfulness/groundedness — does the answer stick to retrieved content? — and answer relevance), often scored with an LLM-as-judge, plus end-to-end task accuracy on real questions.


### M5. What Is "Lost in the Middle," and Why Does It Matter in Prompt Design?

**Lost in the Middle** is a phenomenon where an LLM may pay more attention to information at the beginning and end of a long context than to information in the middle.

In RAG systems, this can cause the LLM to overlook important information when too many document chunks are added to the prompt.

**Why does it matter?**

- **Better context ordering:** Place the most relevant information near the beginning or end of the prompt.
- **Reduce irrelevant content:** Avoid adding too many unnecessary document chunks.
- **Re-ranking:** Rank retrieved chunks by relevance before adding them to the prompt.
- **Improve answer quality:** Help the LLM focus on the most useful information.

**Example:**

Suppose a RAG system retrieves 20 document chunks, and the most important answer is hidden in the middle. The LLM might overlook that information and generate an incomplete answer.

By re-ranking the chunks and placing the most relevant information strategically, we can improve the chances that the LLM uses the correct context.

**In short:** Lost in the Middle reminds us that the order and amount of context in a prompt can affect the quality of an LLM's answer.


**M6. What is agentic / multi-hop RAG?**
Instead of one fixed retrieve-then-generate pass, the model can recognize it needs more information, issue another retrieval query, and iterate — necessary for questions that require combining facts scattered across multiple, non-adjacent sources.


### M7. What Is GraphRAG?

**GraphRAG (Graph-based Retrieval-Augmented Generation)** is an approach that combines RAG with a knowledge graph to retrieve information based on entities and their relationships.

A **knowledge graph** represents information as:
- **Entities:** People, companies, products, or other objects.
- **Relationships:** Connections between entities.

**How does GraphRAG work?**

1. **Extract:** Identifies entities and relationships from documents.
2. **Build:** Creates a knowledge graph connecting related information.
3. **Retrieve:** Finds relevant entities, relationships, or connected information based on the user's question.
4. **Generate:** Provides the retrieved information to the LLM to generate an answer.

**Why do we use GraphRAG?**

- Helps answer complex questions involving multiple documents.
- Identifies relationships between different entities.
- Connects related information that simple chunk-based retrieval might miss.

**Example:**

Suppose a user asks, "Which projects use Kafka, and which companies are responsible for them?"

GraphRAG can connect projects, technologies, and companies through their relationships to help answer the question.

**In short:** Traditional RAG mainly retrieves relevant text chunks, while GraphRAG uses relationships in a knowledge graph to help answer complex, connected questions.


### M8. What Is Query Rewriting/Expansion, and Why Do It Before Retrieval?

**Query rewriting** means changing the user's original question into a clearer query that helps the retrieval system find relevant information.

**Query expansion** means generating additional related queries or alternative phrasings to find more relevant information.

**Why do we use it?**

- **Clearer queries:** Resolves ambiguous questions and missing context.
- **Better retrieval:** Helps find relevant document chunks.
- **Wider search:** Uses different phrasings to retrieve more useful results.
- **Improved accuracy:** Provides more relevant context to the LLM.

**Example:**

Suppose a user asks, "What about its cost?" after discussing the Eiffel Tower.

- **Original query:** "What about its cost?"
- **Rewritten query:** "What was the cost of constructing the Eiffel Tower?"

The rewritten query provides clear context, helping the retrieval system find relevant information.

**In short:** Query rewriting and expansion improve RAG retrieval by making user queries clearer and helping the system find more relevant information.


**M9. How do you decide chunk size and overlap for a given document type — say, legal contracts vs. chat logs?**
There's no universal number — it's tuned empirically against retrieval eval metrics (precision/recall@K) for your actual corpus and query patterns. As a starting intuition: dense, self-contained documents (legal contracts, technical docs) tolerate larger chunks since each paragraph already stands alone; conversational data (chat logs, transcripts) usually needs smaller chunks with overlap, since a single turn out of context is often meaningless. Overlap exists specifically to avoid severing a sentence or idea exactly at a chunk boundary:

```python
def sliding_window_chunks(words, chunk_size, overlap):
    step = chunk_size - overlap
    return [
        " ".join(words[i:i + chunk_size])
        for i in range(0, len(words), step)
        if words[i:i + chunk_size]
    ]

text = "the quick brown fox jumps over the lazy dog near the river bank"
for c in sliding_window_chunks(text.split(), chunk_size=6, overlap=2):
    print(c)
```

Each window re-includes the last `overlap` words of the previous chunk, so a sentence split across the boundary still appears whole in at least one chunk.

**M10. What is re-ranking, and how does a cross-encoder differ from the bi-encoder used for initial retrieval?**
A bi-encoder embeds the query and each chunk independently (query and chunk never see each other), so similarity is just a fast vector-distance lookup — that's what makes ANN search over millions of chunks feasible. A cross-encoder instead reads the query and a single chunk together and outputs a relevance score directly, which is far more accurate but too slow to run against every chunk in the corpus. Re-ranking uses both: bi-encoder retrieval gets a cheap top-N candidate set, then a cross-encoder re-scores just those N before picking the final top-K.

```python
def bi_encoder_score(query_vec, chunk_vec):
    # dot product of two PRECOMPUTED vectors -- cheap, runs against millions of chunks
    return sum(a * b for a, b in zip(query_vec, chunk_vec))

def cross_encoder_score(query_text, chunk_text):
    # toy stand-in for a real cross-encoder network that reads BOTH texts
    # together -- accurate, but far too slow to run against a whole corpus
    shared_words = set(query_text.split()) & set(chunk_text.split())
    return len(shared_words) / max(len(query_text.split()), 1)

query_vec, chunk_vec = [0.2, 0.8, 0.1], [0.3, 0.7, 0.0]
print("bi-encoder (fast, precomputed):", bi_encoder_score(query_vec, chunk_vec))
print("cross-encoder (slow, per-pair):", cross_encoder_score("eiffel tower paris", "the eiffel tower is in paris"))
```

**M11. How do you compute precision@K and recall@K for retrieval evaluation?**
Precision@K is, out of the K chunks you retrieved, what fraction are actually relevant; recall@K is, out of all relevant chunks that exist for that query, what fraction you managed to retrieve in the top K. You need a labeled eval set (query → known relevant chunk ids) to compute either one.

```python
def precision_at_k(retrieved_ids, relevant_ids, k):
    top_k = retrieved_ids[:k]
    hits = sum(1 for cid in top_k if cid in relevant_ids)
    return hits / k

def recall_at_k(retrieved_ids, relevant_ids, k):
    top_k = retrieved_ids[:k]
    hits = sum(1 for cid in top_k if cid in relevant_ids)
    return hits / len(relevant_ids) if relevant_ids else 0.0

retrieved = ["c3", "c1", "c9", "c4"]
relevant = {"c1", "c4", "c7"}
print(precision_at_k(retrieved, relevant, k=4), recall_at_k(retrieved, relevant, k=4))
```

Precision tells you how noisy your top-K is (bloats the prompt with irrelevant chunks); recall tells you whether the answer was even retrievable at all — a generation-quality bug is unfixable if recall@K already missed the one chunk containing the answer.

### Advanced — Bar-Raiser / System-Design Round


### A1. How Would You Design Document-Level Access Control in a RAG System?

**Document-level access control** ensures that users can retrieve only the documents they are authorized to access.

**How does it work?**

1. **Attach permissions:** During document ingestion, store access metadata such as user IDs, group IDs, and roles with each document chunk.
2. **Authenticate the user:** Verify the user's identity using an authentication system such as Keycloak or JWT.
3. **Apply access filters:** Before retrieval, filter the vector database using the user's permissions.
4. **Generate the answer:** Pass only authorized document chunks to the LLM.
5. **Enforce security:** Apply permission checks on every request and prevent unauthorized access to retrieved content.

**Example:**

Suppose a company has two departments: HR and Engineering.

- HR users can access salary and employee documents.
- Engineering users can access technical documentation.
- If an Engineering user asks about employee salaries, the RAG system must not retrieve HR documents.

**Important Security Rule:**

Access control must be enforced at the retrieval layer, not after the LLM generates an answer. Otherwise, unauthorized information could already have been exposed to the model.

**In short:** Store permissions with document chunks and enforce authorization filters during every retrieval request to prevent unauthorized data access.


**A2. How do you keep a RAG index fresh when the underlying data changes frequently?**
Options include incremental re-indexing (only re-embed changed/new documents, tracked via a last-modified timestamp or content hash), a streaming ingestion pipeline for near-real-time updates, and a TTL or versioning scheme so stale chunks are demoted or removed rather than silently lingering forever alongside newer, conflicting information.

**A3. Where does the latency budget go in a production RAG system, and where do you optimize first?**
Roughly: embedding the query (fast, ms), the ANN search (fast if tuned), optional re-ranking (can be the biggest hidden cost if using a cross-encoder over many candidates), and the LLM generation call itself (usually the dominant cost, especially for long outputs). Optimize generation latency first via streaming responses to the user, then re-ranking cost via reducing candidate count, before micro-optimizing the retrieval step.

**A4. How do you evaluate and monitor RAG quality continuously in production, not just offline?**
Sample live traffic and score it with an automated evaluator (faithfulness, relevance) on a rolling basis, track user feedback signals (thumbs down, follow-up rephrasing as an implicit negative signal), and periodically promote interesting production examples — especially failures — into your offline evaluation dataset so it keeps reflecting real usage instead of going stale.

**A5. RAG vs. fine-tuning vs. long-context — when do you choose each, or combine them?**
RAG is best for knowledge that's large, private, or changes frequently — updating it means re-indexing documents, not retraining a model. Fine-tuning is for teaching a fixed behavior — a style, a format, a specific skill — and is a poor tool for injecting facts that change often, since every update means an expensive retrain. Long-context (just pasting everything into the prompt) works when the relevant material is small and stable enough to fit and you'd rather skip retrieval infrastructure entirely. In practice, production systems often combine all three: RAG to fetch relevant material, fed into a model fine-tuned specifically to use retrieved context well (cite sources, refuse when context is insufficient), inside as large a context window as is cost-effective.

**A6. How would you design a RAG system to cite its sources — show which chunk each part of the answer came from?**
Tag every retrieved chunk with a stable id in the prompt itself, instruct the model to cite that id inline in its answer, then post-process the model's output to map cited ids back to real source documents/links for the UI. Critically, verify the model isn't just fabricating plausible-looking citations — at minimum, check that every cited id actually exists among the chunks retrieved for that query, and ideally spot-check that the cited chunk actually supports the sentence next to the citation.

```python
import re

def verify_citations(answer_text, retrieved_chunk_ids):
    cited = set(re.findall(r"\[(\d+)\]", answer_text))
    valid = {cid for cid in cited if int(cid) - 1 in range(len(retrieved_chunk_ids))}
    return {"cited": cited, "fabricated": cited - valid}

answer = "The tower is in Paris [1] and was finished in 1889 [2] per a 1970 survey [5]."
print(verify_citations(answer, retrieved_chunk_ids=["chunkA", "chunkB"]))  # [5] doesn't exist -> fabricated
```

A citation id the model invents that doesn't map to anything actually retrieved is a strong, cheap-to-detect signal of a hallucinated answer.

**A7. How would you implement Reciprocal Rank Fusion (RRF) to combine hybrid search results?**
RRF combines multiple ranked lists (for example, BM25 results and vector-search results) without needing their scores to be on the same scale — it only uses each document's *rank* in each list. Every document gets `1 / (k + rank)` from each list it appears in (k is a small constant, commonly 60, that dampens the impact of low ranks), and the sums become the fused ranking.

```python
def reciprocal_rank_fusion(ranked_lists, k=60):
    scores = {}
    for ranked_list in ranked_lists:
        for rank, doc_id in enumerate(ranked_list, start=1):
            scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + rank)
    return sorted(scores, key=scores.get, reverse=True)

bm25_ranking = ["doc3", "doc1", "doc2"]
vector_ranking = ["doc1", "doc4", "doc3"]
print(reciprocal_rank_fusion([bm25_ranking, vector_ranking]))
```

It's popular precisely because it sidesteps the awkward problem of BM25 scores and cosine similarities living on completely different, hard-to-calibrate numeric scales.

**A8. What happens if you change your embedding model on a production RAG system, and how do you migrate safely?**
Two different embedding models produce vectors in two different, incompatible spaces — a query embedded with model B will not have meaningful cosine similarity to chunks embedded with model A, even though nothing looks obviously broken (the search still returns *some* results, just semantically wrong ones). Safe migration means re-embedding the entire corpus with the new model into a separate index, running both old and new indexes side by side (shadow/blue-green), validating retrieval quality on the new index against your eval set, and only then cutting traffic over — never mixing vectors from two embedding models in one index.

**A9. How do you handle two retrieved chunks that contradict each other — say, an old pricing page and a new one, both still in the index?**
The retrieval layer should give the model the tools to resolve this rather than silently picking one: attach metadata like last-updated timestamps or a source-authority ranking to each chunk, surface it in the prompt, and instruct the model to prefer the more recent/authoritative source or explicitly flag the conflict to the user instead of confidently merging both into one answer. The deeper fix is upstream — the TTL/versioning discussed in the "keeping an index fresh" question (A2) should be demoting or removing the stale document in the first place, so the conflict never reaches retrieval at all.

### Practical / Coding Round

*Questions below reference [`example.py`](example.py), a from-scratch, dependency-free mini RAG pipeline that implements the chunk → embed → index → retrieve → augment → generate flow shown in the diagram above, using bag-of-words term frequency as a clearly-labeled stand-in for real neural embeddings.*

**P1. In `chunk_documents`, what does `chunk_size` control, and what breaks if you set it very high (one chunk per document)?**
`chunk_size` is how many sentences get grouped into a single chunk before it's embedded and indexed. Set it as high as "every sentence in the document" and you're back to whole-document embedding — the Eiffel Tower sentence and the Machu Picchu sentence each blur into one averaged vector per document instead of standing on their own. It also directly feeds the Lost-in-the-Middle problem (M5): a giant single chunk dumped into the prompt buries the one relevant sentence inside a wall of irrelevant text instead of retrieval doing the job of isolating it.

**P2. `embed()` here is bag-of-words term frequency, not a real neural embedding — what specific retrieval failures would you expect that a real embedding model wouldn't have?**
Synonyms score as unrelated — a query about a landmark being "constructed" would completely miss a chunk that says "completed" or "built," since `embed()` only counts literal shared tokens with zero notion of meaning. It also can't handle rewording, word order, or cross-lingual matching, and two chunks about totally different topics that happen to share common filler words ("the," "is," "in") get nonzero similarity purely from noise — all things a real embedding model, trained to place semantically similar text nearby regardless of exact wording, handles naturally.

**P3. `retrieve()` does an O(n) brute-force scan over every chunk — how would you swap in an ANN index instead, and at what corpus size would that actually start to matter?**
You'd replace the linear `for chunk, vec in index` scan with a call into an ANN structure (HNSW, IVF, or a hosted vector database) built once at index time, turning each query from O(n) into roughly O(log n) or better. For a few thousand chunks, brute-force cosine similarity is genuinely fine — often faster than the network round-trip to an external vector database — the crossover point where ANN clearly pays for itself is typically somewhere in the tens-of-thousands-to-millions-of-vectors range, or sooner if query latency budgets are tight.

**P4. `fake_llm()` is a stub — what's the minimal change to call a real LLM API instead, and what would you add for production use?**
Minimally, swap the body of `fake_llm(prompt)` for an actual API call — e.g. `client.messages.create(model=..., messages=[{"role": "user", "content": prompt}])` — and return the response text; the rest of the pipeline (retrieval, prompt-building) doesn't change at all, since `fake_llm` is already isolated behind a single function boundary. For production you'd add retries with backoff for transient failures, a timeout so one slow call can't hang the whole request, streaming so the user sees tokens as they arrive instead of waiting for the full response, and explicit error handling for rate limits and context-length-exceeded errors.

**P5. This pipeline retrieves once and generates once (naive RAG). Sketch how you'd change `if __name__ == "__main__":` to implement one round of multi-hop RAG.**
Retrieve as normal, but before calling `fake_llm` for the final answer, check whether the retrieved chunks actually seem sufficient to answer the question; if not, use the gap to build a refined query and call `retrieve()` a second time, merging the new chunks with the first batch before building the final augmented prompt.

```python
top_k = retrieve(query, index, vocab, k=2)
if not looks_sufficient(query, top_k):           # e.g. ask an LLM, or a similarity-score threshold
    refined_query = f"{query} additional details"   # a real system would generate this with an LLM
    more_chunks = retrieve(refined_query, index, vocab, k=2)
    top_k = top_k + more_chunks                   # dedupe by chunk_id in a real implementation
prompt = build_augmented_prompt(query, top_k)
answer = fake_llm(prompt)
```

This is exactly M6's agentic/multi-hop RAG, just made concrete against this file's actual functions.

**P6. What role does `build_augmented_prompt` play, and what's the risk of blindly concatenating every retrieved chunk into it?**
It's the seam between retrieval and generation — it takes the query plus the scored chunks from `retrieve()` and turns them into the single text string that actually gets sent to the LLM (or to `fake_llm` here), including the citation-style `[1]`, `[2]` labels used by the citation-verification question (A6). The risk of dumping every retrieved chunk in without limits is twofold: you can blow past the model's context window entirely (E3), and even within budget you invite the Lost-in-the-Middle problem (M5) by padding the prompt with marginal chunks instead of keeping it tight and focused on the highest-scoring ones.
