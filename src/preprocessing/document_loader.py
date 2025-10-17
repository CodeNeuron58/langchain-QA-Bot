from langchain_community.document_loaders import PyPDFLoader
import tempfile

def document_loader(file):
    """Load PDF document."""
    # loader = PyPDFLoader(file.name)
    # return loader.load()

    # Save the uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(file.getbuffer())
        tmp_path = tmp_file.name

    loader = PyPDFLoader(tmp_path)
    loaded_document = loader.load()

    return loaded_document