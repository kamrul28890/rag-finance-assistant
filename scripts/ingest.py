import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

DATA_DIR = "data/finance_docs"
EMBED_DIR = "embeddings"

load_dotenv()

def load_documents():
    docs = []
    for file in os.listdir(DATA_DIR):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(DATA_DIR, file))
            docs.extend(loader.load())
    return docs

def split_documents(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_documents(docs)

def embed_documents(docs):
    embeddings = HuggingFaceEmbeddings(model_name="./paraphrase-MiniLM-L6-v2")
    db = FAISS.from_documents(docs, embeddings)
    db.save_local("embeddings")
    print("✅ Embeddings saved to 'embeddings/'")


if __name__ == "__main__":
    raw_docs = load_documents()
    split_docs = split_documents(raw_docs)
    embed_documents(split_docs)
