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


def alternatingly_agree(message, history):
    if len(history) % 2 == 0:
        return f"Yes, I do think that '{message}'"
    else:
        return "I don't think so"

gr.ChatInterface(alternatingly_agree).launch()