# 🤖 AI Customer Support Platform

An end-to-end **Agentic AI Customer Support Platform** built with **FastAPI**, **Google Gemini**, **Hybrid RAG**, and **PostgreSQL**.

Instead of relying on a single chatbot prompt, the system follows an **Agent-Oriented Architecture** where an AI planner dynamically decides which tool should solve the user's request.

The platform combines:

- 📚 Retrieval-Augmented Generation (Hybrid RAG)
- 🤖 Agentic Tool Calling
- 🗄 PostgreSQL Integration
- 📦 Order Management
- 🎫 Ticket Management
- 📧 Email Generation
- 📊 SQL Analytics
- 📈 Evaluation Framework

---

# ✨ Features

## 🤖 Agent Architecture

The AI agent can reason about a user's request and dynamically choose the appropriate tool.

Available tools:

- Knowledge Search
- Order Lookup
- Ticket Lookup
- SQL Analytics
- Email Generation

---

## 📚 Hybrid RAG Pipeline

The knowledge retrieval system combines multiple retrieval techniques for better accuracy.

Implemented features:

- Hybrid Search (FAISS + BM25)
- Query Rewriting
- Multi Query Retrieval
- Cross Encoder Reranking
- Context Compression
- Retrieval Evaluation

---

## 🗄 Structured Data Support

Structured customer information is stored inside PostgreSQL.

Current entities:

- Orders
- Support Tickets
- Users
- Conversations
- Messages

Database migrations are managed using **Alembic**.

---

## 📊 SQL Analytics Tool

The SQL Tool allows the agent to answer analytical questions over structured data.

Examples:

```
How many shipped orders are there?

Show cancelled orders.

Show open tickets.

List high priority tickets.
```

Instead of allowing arbitrary SQL execution, the system converts supported natural language questions into predefined SQL queries.

---

## 📧 Email Generation

The Email Tool automatically generates customer support emails using the collected conversation context.

---

## 📈 Evaluation Framework

The project includes retrieval evaluation metrics:

- Hit Rate
- Precision
- Mean Reciprocal Rank (MRR)

and an extensible agent evaluation framework.

---

# 🏗 System Architecture

```
                          User
                           │
                           ▼
                     AI Planner
                           │
      ┌────────────┬────────────┬────────────┬────────────┬────────────┐
      ▼            ▼            ▼            ▼            ▼
Knowledge      Order Tool   Ticket Tool   SQL Tool    Email Tool
 Search             │            │            │            │
      │             ▼            ▼            ▼            │
      ▼       PostgreSQL   PostgreSQL   PostgreSQL        │
 Hybrid RAG            \         |         /              │
                        └─────────┴─────────┘
                               │
                               ▼
                      Response Generator
                               │
                               ▼
                            User
```

---

# 🔍 Retrieval Pipeline

```
User Question
      │
      ▼
Query Rewriting
      │
      ▼
Multi Query Generation
      │
      ▼
Hybrid Retrieval
(FAISS + BM25)
      │
      ▼
Cross Encoder Reranking
      │
      ▼
Context Compression
      │
      ▼
Gemini
```

---

# 🛠 Tech Stack

## Backend

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic

## AI / LLM

- Google Gemini
- Sentence Transformers
- Cross Encoder
- FAISS
- Rank-BM25

## Agent

- Planner
- Orchestrator
- Observer
- Tool Registry
- Context Manager
- History Manager
- Tool Executor

## Evaluation

- Hit Rate
- Precision
- Mean Reciprocal Rank (MRR)

---

# 📂 Project Structure

```
ai-support-platform/

├── alembic/
│
├── app/
│   ├── agent/
│   ├── api/
│   ├── auth/
│   ├── database/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── tests/
│   ├── logger.py
│   └── main.py
│
├── data/
│
├── evaluation/
│
├── knowledge_base/
│
├── scripts/
│
├── requirements.txt
│
└── README.md
```

---

# 🚀 Getting Started

## 1. Clone the repository

```bash
git clone https://github.com/<your-username>/ai-support-platform.git

cd ai-support-platform
```

---

## 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure environment variables

Create a `.env` file.

Example:

```env
GOOGLE_API_KEY=your_gemini_api_key

DATABASE_URL=postgresql://username:password@localhost:5432/ai_support_db
```

---

## 5. Run database migrations

```bash
alembic upgrade head
```

---

## 6. Import demo data

```bash
python -m scripts.import_orders

python -m scripts.import_tickets
```

---

## 7. Start the FastAPI server

```bash
uvicorn app.main:app --reload
```

---

# 💬 Example Questions

### Knowledge

```
Can I get a refund?

How long does express shipping take?

What is your warranty policy?
```

### Orders

```
Track order ORD1001.

Where is my order?
```

### Tickets

```
Check ticket TKT1001.

What is the status of my support request?
```

### SQL Analytics

```
How many shipped orders are there?

Show cancelled orders.

Show open tickets.

List high priority tickets.
```

### Email

```
Send an email to customer@example.com
```

---

# ✅ Current Project Status

- ✔ Hybrid RAG
- ✔ Query Rewriting
- ✔ Multi Query Retrieval
- ✔ Cross Encoder Reranking
- ✔ Context Compression
- ✔ Planner
- ✔ Orchestrator
- ✔ Observer
- ✔ Tool Registry
- ✔ Knowledge Tool
- ✔ Order Tool
- ✔ Ticket Tool
- ✔ SQL Tool
- ✔ Email Tool
- ✔ PostgreSQL Integration
- ✔ Alembic Migrations
- ✔ Retrieval Evaluation
- ✔ Agent Evaluation Framework

---

# 🔮 Future Improvements

- Conversation Memory Integration
- React Frontend
- Docker Support
- CI/CD Pipeline
- Authentication & Role-Based Access
- Streaming Responses
- Deployment to Cloud

---

# 👨‍💻 Author

**Prasad Kadam**

This project was built to explore modern **GenAI Engineering**, combining Retrieval-Augmented Generation, Agentic AI, tool orchestration, structured data querying, and evaluation into a production-oriented customer support platform.