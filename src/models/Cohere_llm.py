from langchain_cohere import ChatCohere
import os
from dotenv import load_dotenv

import yaml

load_dotenv()

cohere_api_key = os.getenv("COHERE_API_KEY")
if not cohere_api_key:
    raise ValueError("COHERE_API_KEY not found in .env file or environment")



with open('params.yaml', 'r') as file:
    config = yaml.safe_load(file)
def get_llm():
    """Initialize and return the Cohere LLM model."""
    
    llm = ChatCohere(
        cohere_api_key= cohere_api_key,
        model= config['Cohere_LLM']['model'],
    )
    return llm
