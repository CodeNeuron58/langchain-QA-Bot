from langchain.chains import RetrievalQA
from src.models.Cohere_llm import get_llm
from core.retriever import get_retriever

def retriever_qa(file, query):
    """Execute the RAG QA chain."""
    llm = get_llm()
    retriever_obj = get_retriever(file)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever_obj,
        return_source_documents=False
    )
    response = qa_chain.invoke(query)
    return response["result"]
