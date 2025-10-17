import streamlit as st
from core.QA_chain import retriever_qa
from io import BytesIO


# -----------------------
# Streamlit Configuration
# -----------------------
st.set_page_config(
    page_title="RAG Chatbot",
    page_icon="🤖",
    layout="wide"
)

# -----------------------
# Sidebar Configuration
# -----------------------
st.sidebar.header("⚙️ Configuration")
st.sidebar.markdown("""
This RAG chatbot uses:
- **Cohere LLM** (Mixtral)
- **Hugging Face Embeddings**
- **Chroma Vector DB**
""")
st.sidebar.markdown("---")
st.sidebar.markdown("Developed by **Biprayan**")

# -----------------------
# Main Title
# -----------------------
st.title("📄 RAG-Powered Document Chatbot")
st.markdown(
    "Upload a **PDF document**, then ask any question about its contents. "
    "The model retrieves relevant chunks and answers using **LLM reasoning**."
)

# -----------------------
# File Upload Section
# -----------------------
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

# -----------------------
# Chat Interface
# -----------------------
if uploaded_file is not None:
    st.success("✅ File uploaded successfully!")

    query = st.text_area("Ask your question:", placeholder="Type your query here...")
    # ensure processing flag exists in session_state
    if "processing" not in st.session_state:
        st.session_state.processing = False

    # disable the button while processing to avoid duplicate runs
    if st.button("Get Answer", disabled=st.session_state.processing):
        st.session_state.processing = True
        with st.spinner("Processing... Please wait."):
            try:
                # Process the file and query without caching
                file_bytes = uploaded_file.getbuffer().tobytes()
                f = BytesIO(file_bytes)
                f.name = uploaded_file.name
                answer = retriever_qa(f, query)
                st.subheader("💬 Answer:")
                st.write(answer)

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

            finally:
                # reset processing flag so button is usable again
                st.session_state.processing = False

else:
    st.warning("Please upload a PDF to begin.")

# -----------------------
# Footer
# -----------------------
st.markdown("---")
st.caption("Built with ❤️ using Streamlit and Langchain.")

