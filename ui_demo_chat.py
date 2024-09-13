import gradio as gr
from llama_index.llms.lmstudio import LMStudio

llm = LMStudio(
    model_name="Hermes-2-Pro-Llama-3-8B",
    base_url="http://localhost:1234/v1",
    temperature=0.7,
)

# Define function to handle user queries and return responses from the model
def get_llm_response(user_message, history):
    response = llm.complete(user_message)  
    return str(response)  # Returning the generated response from the LLM

# Initialize the Gradio ChatInterface
with gr.Blocks() as demo:
    chatbot = gr.ChatInterface(
        fn=get_llm_response,  # Function to call when the user submits a message
        title="LMStudio Chatbot"
    )

# Launch the Gradio app
demo.launch()

