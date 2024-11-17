from llama_index.llms.lmstudio import LMStudio
from llama_index.core.base.llms.types import ChatMessage, MessageRole

llm = LMStudio(
    model_name="llama-3.2-3b-instruct",
    base_url="http://localhost:1234/v1",
    temperature=0.7,
)

response = llm.complete("Hey there, what is 2+2?")
print(str(response))

response = llm.stream_complete("What is 7+3?")
for r in response:
    print(r.delta, end="")

messages = [
    ChatMessage(
        role=MessageRole.SYSTEM,
        content="You an expert AI assistant. Help User with their queries.",
    ),
    ChatMessage(
        role=MessageRole.USER,
        content="What is the significance of the number 42?",
    ),
]

response = llm.chat(messages=messages)
print(str(response))

response = llm.stream_chat(messages=messages)
for r in response:
    print(r.delta, end="")