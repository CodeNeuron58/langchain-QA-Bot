from langchain_chroma import Chroma
from src.models.HF_embeddings import HuggingFace_embedding

def vector_database(chunks):
    """Create vector database from chunks."""
    embedding_model = HuggingFace_embedding()
    return Chroma.from_documents(chunks, embedding_model)