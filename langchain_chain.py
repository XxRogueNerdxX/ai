from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda
from langchain_openai import ChatOpenAI

from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate   


model = ChatOllama(model="qwen2.5:0.5b")

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "Be an helpful AI assistant and help"), 
        ("human", "What's the capital of {country}")
    ]
)

def word_count(x): 
    print(x) 
    return len(x)

uppercase_output = RunnableLambda(lambda x: x.upper())
count_words = RunnableLambda(lambda x: word_count(x))


chain = prompt_template | model | StrOutputParser() | uppercase_output | count_words

result = chain.invoke({"country":"france"})
print(result)