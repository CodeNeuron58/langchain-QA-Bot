import gradio as gr
from core.QA_chain import retriever_qa
# from utils.suppress_warnings import suppress_all_warnings
# from config.settings import SERVER_NAME, SERVER_PORT

# suppress_all_warnings()

rag_app = gr.Interface(
    fn=retriever_qa,
    allow_flagging="never",
    inputs=[
        gr.File(label="Upload PDF File", file_count="single", file_types=['.pdf']),
        gr.Textbox(label="Input Query", lines=2, placeholder="Type your question here...")
    ],
    outputs=gr.Textbox(label="Output"),
    title="RAG Chatbot",
    description="Upload a PDF document and ask questions based on its content."
)

if __name__ == "__main__":
    
    rag_app.launch()
    
