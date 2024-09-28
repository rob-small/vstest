import gradio as gr
from library import Library

# Initialize the Library instance
library = Library()

def add_book(title: str) -> str:
    """
    Adds a book to the library's collection. Do not add the same book twice. Only add a book if explicitly requested by the user.

    Parameters:
    title (str): The title of the book to add.

    Returns:
    str: A message indicating that the book was added.
    """
    library.add_book(title)
    return f"Added book: {title}"

def check_out(title: str) -> bool:
    """
    Checks out a book from the library's collection. Pnly check out a book if explicitly requested by the user.

    Parameters:
    title (str): The title of the book to check out.

    Returns:
    str: A message indicating whether the book was successfully checked out.
    """
    success = library.check_out(title)
    return f"Checked out '{title}': {success}"

def check_in(title: str) -> bool:
    """
    Checks a book back into the library's collection. Only check in a book if explicitly requested by the user.

    Parameters:
    title (str): The title of the book to check in.

    Returns:
    str: A message indicating whether the book was successfully checked in.
    """

    success = library.check_in(title)
    return f"Checked in '{title}': {success}"

def is_available(title: str) -> bool:
    """
    Checks if a book is available in the library's collection.

    Parameters:
    title (str): The title of the book to check.

    Returns:
    str: A message indicating whether the book is available.
    """
    available: bool = library.is_available(title)
    return f"'{title}' is available: {available}"
def list_available_books() -> str:
    """
    Lists all books in the library collections that are currently available.

    Returns:
    str: A string of book titles, separated by newline characters.
    """
    return library.list_books()

library.add_book("The Catcher in the Rye")
library.add_book("To Kill a Mockingbird")
library.add_book("1984")
library.add_book("Pride and Prejudice")

from llama_index.llms.lmstudio import LMStudio
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import FunctionTool
from llama_index.core import PromptTemplate

from  library_ui_prompt import react_system_header_str

react_system_prompt = PromptTemplate(react_system_header_str)

llm = LMStudio(
    model_name="lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf",
    base_url="http://localhost:1234/v1",
    temperature=0.7,
)

add_book = FunctionTool.from_defaults(fn=add_book )
check_out = FunctionTool.from_defaults(fn=check_out)
check_in = FunctionTool.from_defaults(fn=check_in)
is_available = FunctionTool.from_defaults(fn=is_available)
list_books = FunctionTool.from_defaults(fn=list_available_books)

agent = ReActAgent.from_tools([add_book, check_out, check_in, is_available, list_books], llm=llm, verbose=True, max_iterations=50)
agent.update_prompts({"agent_worker:system_prompt": react_system_prompt})

# Define function to handle user queries and return responses from the model
def get_llm_response(user_message, history):
    response = agent.chat(user_message)  
    return str(response)  # Returning the generated response from the LLM

# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Library Management System")

    with gr.Tab("Add Book"):
        title_input = gr.Textbox(label="Title")
        add_book_button = gr.Button("Add Book")
        add_book_output = gr.Textbox(label="Output")
        add_book_button.click(add_book, inputs=[title_input], outputs=add_book_output)

    with gr.Tab("Check Out Book"):
        title_input = gr.Textbox(label="Title")
        check_out_button = gr.Button("Check Out")
        check_out_output = gr.Textbox(label="Output")
        check_out_button.click(check_out, inputs=title_input, outputs=check_out_output)

    with gr.Tab("Check In Book"):
        title_input = gr.Textbox(label="Title")
        check_in_button = gr.Button("Check In")
        check_in_output = gr.Textbox(label="Output")
        check_in_button.click(check_in, inputs=title_input, outputs=check_in_output)

    with gr.Tab("Check Availability"):
        title_input = gr.Textbox(label="Title")
        check_availability_button = gr.Button("Check Availability")
        check_availability_output = gr.Textbox(label="Output")
        check_availability_button.click(is_available, inputs=title_input, outputs=check_availability_output)

    with gr.Tab("List Books"):
        list_books_button = gr.Button("List Books")
        list_books_output = gr.Textbox(label="Books", interactive=False,lines=5)
        list_books_button.click(list_books, outputs=list_books_output)

    with gr.Tab("Chat with Agent"):
        chatbot = gr.ChatInterface(
            fn=get_llm_response
        )

# Launch the app
demo.launch()