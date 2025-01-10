from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableParallel, RunnableBranch
from langchain_openai import ChatOpenAI

from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate   


model = ChatOllama(model="qwen2.5:0.5b")

positive_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an helpful assitant"), 
        ("human", "Generate a thank you note for this positive feedback: {feedback}")
    ]
)

negative_feedback_template = ChatPromptTemplate.from_mesasges(
    [
        ("system", "You are an helpful assitant"), 
        ("human", "Generate a thank you note for this negative feedback: {feedback}")
    ]
)

neutral_feedback_template = ChatPromptTemplate.from_mesasges(
    [
        ("system", "You are an helpful assitant"), 
        ("human", "Generate a thank you note for this neutral feedback: {feedback}")
    ]
)

escalate_feedback_template = ChatPromptTemplate.from_mesasges(
    [
        ("system", "You are an helpful assitant"), 
        ("human", "Generate a message to escalate this feedback to a human agent: {feedback}")
    ]
)

classification_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an helpful assitant"), 
        ("human", "Classify the sentiment of this feedback as positive, negative, neutral or escalate: {feedback}")
    ]
)

branches = RunnableBranch(
    (
        lambda x: "positive" in x, 
        positive_feedback_template | model | StrOutputParser()
    ), 
    (
        lambda x: "negative" in x, 
        negative_feedback_template | model | StrOutputParser() 
    )
)
