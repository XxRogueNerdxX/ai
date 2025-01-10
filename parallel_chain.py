from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableParallel
from langchain_openai import ChatOpenAI

from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate   

model = ChatOllama(model = "qwen2.5:0.5b")
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert product reviewer"), 
        ("human", "List the main features of the product {product_name}")
    ]
)

def analyze_pros(features): 
    pros = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an expert product reviewer"), 
            ("human", "Given these {features} list the pros of these")

        ]
    )

    return pros 

def analyze_cons(features): 
    cons = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an expert product reviewr"), 
            ("human", "Given these features {features} list the cons of the features")
        ]
    )

    return cons 
pros_branch = (
    RunnableLambda(lambda x: analyze_pros(x)) | model | StrOutputParser() 
)

cons_branch = (
    RunnableLambda(lambda x: analyze_cons(x)) |  model | StrOutputParser() 
)

def combine_pros_cons(pros, cons): 
    print(f"{pros}, {cons}")

chain = (
    prompt_template 
    | model | StrOutputParser() 
    | RunnableParallel(branches={"pros": pros_branch, "cons":cons_branch })
    | RunnableLambda(lambda x: combine_pros_cons(x["branches"]["pros"], 
                                                 x["branches"]["cons"]))
)

result = chain.invoke({"product_name": "Macbook"})
print(result)
