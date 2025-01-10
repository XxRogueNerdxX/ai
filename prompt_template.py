from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate   


messages = [
    ("system", "You are a helpful assistant. Please response to the user queries"),
    ("blah", "Questions: What's the capital of {country}?")
]

prompt_template = ChatPromptTemplate.from_messages(messages)
prompt  = prompt_template.invoke({"country":"France"})
print(prompt)

# model = ChatOllama(model="qwen2.5:0.5b")
