from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os 
from dotenv import load_dotenv

os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = os.getenv('LANGCHAIN_TRACING_V2')
load_dotenv()

# print(os.environ['LANGCHAIN_API_KEY'] )
# print(os.environ['LANCHAIN_TRACING_V2'] )

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please resposne to the use queries "), 
        ("user", "Questions:{question}")
    ]
)

# st.title("Langchain demo")
# input_text = st.text_input("Search the topic you want")

llm = Ollama(model="qwen2.5:0.5b")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

input_text = "Hello"
chain.invoke({"question":input_text})
# if input_text: 
    # st.write(chain.invoke({"question":input_text}))