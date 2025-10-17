from langchain.text_splitter import RecursiveCharacterTextSplitter
import yaml

with open('params.yaml', 'r') as file:
    config = yaml.safe_load(file)
def text_splitter(documents):
    """Split documents into manageable chunks."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=config['Text_splitting']['chunk_size'],
        chunk_overlap=config['Text_splitting']['chunk_overlap'],
    )
    return splitter.split_documents(documents)
