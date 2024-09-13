import gradio as gr
from llama_index.core.agent import ReActAgent
from llama_index.llms.lmstudio import LMStudio


# Initialize the language model
llm = LMStudio(
    model_name="Hermes-2-Pro-Llama-3-8B",
    base_url="http://localhost:1234/v1",
    temperature=0.7,
)

# Create the agent
agent = ReActAgent.from_llm(llm=llm, verbose=True, max_iterations=50)

# Define the function for interacting with the agent
def chat_with_agent(user_input):
    # The agent will use the provided input to generate a response
    response = agent.chat(user_input)
    return response

# Create the Gradio interface
iface = gr.Interface(
    fn=chat_with_agent,
    inputs="text",
    outputs="text",
    title=" Agent Chat",
    description="Chat with the library agent to ask questions or perform actions."
)

# Launch the Gradio interface
iface.launch()
