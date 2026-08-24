# GenAI & Agentic AI Interview Prep

**Generative AI, RAG, and agentic systems** are now a standard interview topic at MNCs and product companies, alongside classic DSA. This folder is a from-scratch-to-advanced reference covering the concepts, the data flow behind each one, 30+ interview Q&A per topic, and a runnable Python example per topic.

## Topics

| # | Topic | Folder | Diagram | Asked At |
|---|---|---|---|---|
| 1 | Generative AI | [01_generative_ai/](01_generative_ai/) | Autoregressive generation loop | Amazon, Google, Microsoft, Meta |
| 2 | Embeddings | [02_embeddings/](02_embeddings/) | Meaning → vector space | Amazon, Google, Meta |
| 3 | Vector Databases | [03_vector_databases/](03_vector_databases/) | Ingestion + query pipeline | Amazon, Google, Microsoft |
| 4 | RAG | [04_rag/](04_rag/) | Offline ingestion + runtime pipeline | Amazon, Google, Microsoft, Meta |
| 5 | LangChain | [05_langchain/](05_langchain/) | LCEL chain composition | Amazon, Microsoft, product startups |
| 6 | LangGraph | [06_langgraph/](06_langgraph/) | Stateful loop / graph | Amazon, Microsoft, product startups |
| 7 | Agentic AI | [07_agentic_ai/](07_agentic_ai/) | ReAct think-act-observe loop | Amazon, Google, Microsoft, Meta |
| 8 | Deep Agents | [08_deep_agents/](08_deep_agents/) | Orchestrator + sub-agents + planning | Anthropic, Google, Microsoft |
| 9 | LangSmith | [09_langsmith/](09_langsmith/) | Tracing + evaluation | Amazon, Microsoft, product startups |

## How Each Topic Folder Is Organized

Every topic is its own folder with two files:

- **`interview_qa.md`** — Overview in plain English, a Mermaid data-flow diagram (renders natively on GitHub and in VS Code's Markdown preview), and 30+ interview Q&A in four tiers that mirror how an MNC interview loop actually escalates, with short Python snippets woven into answers where a snippet explains the mechanism better than prose:
  - **Easy — Screening Round** (`E#`) — definitions and basic mechanics.
  - **Medium — Technical Round** (`M#`) — comparisons, trade-offs, "how does X work under the hood."
  - **Advanced — Bar-Raiser / System-Design Round** (`A#`) — production scale, cost, security, failure modes.
  - **Practical / Coding Round** (`P#`) — hands-on questions that reference the actual functions in that topic's `example.py`.
- **`example.py`** — a runnable, dependency-light Python file implementing the topic's core mechanism from scratch (LangChain/LangGraph topics use the real library with an offline fake model, so no API key is ever required). Run it directly, e.g.:

```bash
python 01_generative_ai/example.py
```

Read top to bottom the first time — the topics build on each other: an LLM (01) becomes useful over your own data once it can retrieve from a vector index (02–03); retrieval becomes RAG (04); RAG gets composed into apps with LangChain (05); LangChain's linear chains get upgraded into looping, stateful agents with LangGraph (06) — which is what makes agentic behavior (07) possible; long, multi-step agent work gets a dedicated pattern with Deep Agents (08); and LangSmith (09) is what lets you see and evaluate all of it in production.

## Folder Structure

```
genai_interview_prep/
├── README.md
├── 01_generative_ai/
│   ├── interview_qa.md
│   └── example.py
├── 02_embeddings/
│   ├── interview_qa.md
│   └── example.py
├── 03_vector_databases/
│   ├── interview_qa.md
│   └── example.py
├── 04_rag/
│   ├── interview_qa.md
│   └── example.py
├── 05_langchain/
│   ├── interview_qa.md
│   └── example.py
├── 06_langgraph/
│   ├── interview_qa.md
│   └── example.py
├── 07_agentic_ai/
│   ├── interview_qa.md
│   └── example.py
├── 08_deep_agents/
│   ├── interview_qa.md
│   └── example.py
└── 09_langsmith/
    ├── interview_qa.md
    └── example.py
```
