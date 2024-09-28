from library import Library

the_library = Library()
the_library.add_book("The Catcher in the Rye")
the_library.add_book("To Kill a Mockingbird")
the_library.add_book("1984")
the_library.add_book("Pride and Prejudice")
print(the_library.list_books())

from llama_index.core.agent import ReActAgent
from llama_index.core.tools import FunctionTool
from llama_index.llms.lmstudio import LMStudio

llm = LMStudio(
    model_name="lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf",
    base_url="http://localhost:1234/v1",
    temperature=0.7,
)

add_book = FunctionTool.from_defaults(fn=the_library.add_book)
check_out = FunctionTool.from_defaults(fn=the_library.check_out)
check_in = FunctionTool.from_defaults(fn=the_library.check_in)
is_available = FunctionTool.from_defaults(fn=the_library.is_available)
list_books = FunctionTool.from_defaults(fn=the_library.list_books)

agent = ReActAgent.from_tools([add_book, check_out, check_in, is_available, list_books], llm=llm, verbose=True, max_iterations=50)


prompt_dict = agent.get_prompts()
for k, v in prompt_dict.items():
    print(f"Prompt: {k}\n\nValue: {v.template}")

response = agent.chat("Show me a list of all the books in the library collection. Use the list_books tool to check.")

print(response) 

