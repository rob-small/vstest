import gradio as gr
from library import Library

# Initialize the Library instance
library = Library()

def add_book(title, author):
    library.add_book(title, author)
    return f"Added book: {title} by {author}"

def check_out(title):
    success = library.check_out(title)
    return f"Checked out '{title}': {success}"

def check_in(title):
    success = library.check_in(title)
    return f"Checked in '{title}': {success}"

def is_available(title):
    available = library.is_available(title)
    return f"'{title}' is available: {available}"

def list_books():
    return library.list_books()

library.add_book("The Catcher in the Rye", "J. D. Salinger")
library.add_book("To Kill a Mockingbird", "Harper Lee")
library.add_book("1984", "George Orwell")
library.add_book("Pride and Prejudice", "Jane Austen")

# Gradio interface
with gr.Blocks() as app:
    gr.Markdown("# Library Management System")

    with gr.Tab("Add Book"):
        title_input = gr.Textbox(label="Title")
        author_input = gr.Textbox(label="Author")
        add_book_button = gr.Button("Add Book")
        add_book_output = gr.Textbox(label="Output")
        add_book_button.click(add_book, inputs=[title_input, author_input], outputs=add_book_output)

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
        list_books_output = gr.Textbox(label="Books", interactive=False)
        list_books_button.click(list_books, outputs=list_books_output)

# Launch the app
app.launch()