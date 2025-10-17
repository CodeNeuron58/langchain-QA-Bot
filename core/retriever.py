from src.preprocessing.document_loader import document_loader
from src.preprocessing.doc_splitter import text_splitter
from src.preprocessing.vector_store import vector_database

def get_retriever(file):
    """Create retriever from a PDF file."""
    documents = document_loader(file)
    chunks = text_splitter(documents)
    vectordb = vector_database(chunks)
    retriever = vectordb.as_retriever()
    return retriever


