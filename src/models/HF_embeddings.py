from langchain_huggingface import HuggingFaceEmbeddings
import yaml

with open('params.yaml', 'r') as file:
    config = yaml.safe_load(file)

def HuggingFace_embedding():
    """Return HuggingFace embedding model instance."""
    return HuggingFaceEmbeddings(
        model_name=config['Embeddings']['model_name'],
    )
