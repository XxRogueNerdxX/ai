from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


model = ChatOllama(model="qwen2.5:0.5b")

messages = [
    SystemMessage("You are a helpful assistant. Please response to the user queries"),
    HumanMessage("Questions: What's the capital of France?")
]

# result = model.invoke(messages)
# print(result.content)
state = [] 
system_msg = SystemMessage("You are a helpful assistant. Please response to the user queries")
state.append(system_msg)
while True: 
    data = input("Enter your question: ")
    if data == "exit":
        break
    human_msg = HumanMessage(data)
    state.append(human_msg)
    result = model.invoke(state)
    print(result.content)
    state.append(AIMessage(result.content))


