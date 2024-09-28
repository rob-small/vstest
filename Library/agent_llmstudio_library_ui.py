import gradio as gr
from library import Library
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import FunctionTool
from llama_index.llms.lmstudio import LMStudio

# Initialize the library and add books
the_library = Library()
the_library.add_book("The Catcher in the Rye", "J. D. Salinger")
the_library.add_book("To Kill a Mockingbird", "Harper Lee")
the_library.add_book("1984", "George Orwell")
the_library.add_book("Pride and Prejudice", "Jane Austen")

# Initialize the language model
llm = LMStudio(
    model_name="Hermes-2-Pro-Llama-3-8B",
    base_url="http://localhost:1234/v1",
    temperature=0.7,
)

# Map the library's functions to tools the agent can use
add_book = FunctionTool.from_defaults(fn=the_library.add_book)
check_out = FunctionTool.from_defaults(fn=the_library.check_out)
check_in = FunctionTool.from_defaults(fn=the_library.check_in)
is_available = FunctionTool.from_defaults(fn=the_library.is_available)
list_books = FunctionTool.from_defaults(fn=the_library.list_books)

# Create the agent
agent = ReActAgent.from_tools([add_book, check_out, check_in, is_available, list_books], llm=llm, verbose=True, max_iterations=50)

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
    title="Library Agent Chat",
    description="Chat with the library agent to ask questions or perform actions."
)

# Launch the Gradio interface
iface.launch()
