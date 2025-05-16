from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from dotenv import load_dotenv
import os

load_dotenv()

def get_rag_chain():
    embeddings = HuggingFaceEmbeddings(model_name="./paraphrase-MiniLM-L6-v2")
    db = FAISS.load_local("embeddings", embeddings, allow_dangerous_deserialization=True)
    retriever = db.as_retriever()
    retriever.search_kwargs['k'] = 2  # Limit number of chunks to avoid token overflow

    model_name = "./flan-t5-base"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer, max_length=512)
    llm = HuggingFacePipeline(pipeline=pipe)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    return qa_chain
