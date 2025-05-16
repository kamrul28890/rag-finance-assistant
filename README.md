# 💼 RAG-Based Finance Assistant (Offline)

A local, offline Retrieval-Augmented Generation (RAG) assistant that answers finance-related questions using your own PDF documents.

Built with:
- 🧠 [LangChain](https://www.langchain.com/)
- 🧲 [FAISS](https://github.com/facebookresearch/faiss)
- 🧬 [Hugging Face Transformers](https://huggingface.co/)
- 📄 PyPDF for PDF parsing

---

## ✨ Features

- 🔍 Search through financial reports using semantic similarity
- 🧠 Answer questions like "Who is the auditor?" or "What is the net income?"
- 💾 100% offline — no API keys or internet required once setup is complete
- 🔐 Safe and private: your data never leaves your machine

---

## 📁 Folder Structure

```bash
rag-finance-assistant/
├── scripts/
│   ├── ingest.py           # Load, split, embed PDFs
│   ├── rag_pipeline.py     # Build RAG chain
│   └── main.py             # CLI interface
├── data/finance_docs/      # Place your PDFs here
├── embeddings/             # Saved FAISS vector DB (auto-created)
├── flan-t5-base/           # Downloaded seq2seq model
├── paraphrase-MiniLM-L6-v2/ # Downloaded embedding model
├── .env                    # Environment variables
└── requirements.txt        # Dependencies
```

---

## 🚀 Setup Instructions

### 1. 🔧 Clone the Repo

```bash
git clone https://github.com/your-username/rag-finance-assistant.git
cd rag-finance-assistant
```

### 2. 🐍 Create & Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # For Windows
```

### 3. 📆 Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. 📁 Add Finance Documents

Put your PDF reports inside the following folder:

```bash
data/finance_docs/
```

> You can include balance sheets, earnings reports, annual financials, etc.

---

### 5. 📅 Download Models Offline

> These are large — use `git lfs` or clone directly using HTTPS

```bash
# Install Git LFS if you haven’t
git lfs install

# Clone embedding model
git clone https://huggingface.co/sentence-transformers/paraphrase-MiniLM-L6-v2

# Clone text-generation model
git clone https://huggingface.co/google/flan-t5-base
```

Place both folders in the **root** of the repo.

---

### 6. 🔐 Create `.env` File

Create a `.env` file in the project root:

```env
HUGGINGFACEHUB_API_TOKEN=your_token_here  # Optional, only needed for online mode
```

For offline use, this can be blank or skipped.

---

## 🧠 Run the Pipeline

### Step 1: Ingest Documents

```bash
python scripts/ingest.py
```

This will:
- Load your PDFs
- Split them into chunks
- Embed them using the local model
- Save the FAISS index in `embeddings/`

### Step 2: Start Chat Interface

```bash
python scripts/main.py
```

You’ll see:

```
💬 Finance Assistant Ready. Type your question (type 'exit' to quit):
>
```

Try asking:
- "What is the total revenue?"
- "Who audited the report?"
- "Summarize the income statement."

---

## 🧪 Example Output

```
> What is the net income for 2023?

Answer: The net income reported for 2023 is $8.2 million.
```

---

## 🛡️ Notes

- Runs fully offline after setup — safe for confidential financial data
- Works on Windows, macOS, or Linux (Python 3.9+ recommended)
- Can be extended to support CSV, DOCX, or website data

---

## 🛠️ Future Improvements

- Web UI (e.g., Streamlit)
- Citation of document sources
- Memory support for multi-turn Q&A

---

## 📄 License

MIT License. Use freely. Attribution appreciated.

---

## 🤝 Contributions

PRs and ideas welcome! Feel free to fork or open issues.
