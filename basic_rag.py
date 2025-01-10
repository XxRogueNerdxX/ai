import os 
from dotenv import load_dotenv

os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = os.getenv('LANGCHAIN_TRACING_V2')
load_dotenv()

import bs4 
from langchain import hub 
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_ollama import OllamaEmbeddings


loader = WebBaseLoader(
    web_paths= ("https://lilianweng.github.io/posts/2023-06-23-agent/",), 
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
            class_ =("post-content", "post-title", "post-header")
        )
    )
)

docs = loader.load() 

text_splitter = RecursiveCharacterTextSplitter( chunk_size =1000, chunk_overlap=2000)
splits = text_splitter.split_documents(docs)

embeddings = OllamaEmbeddings(
    model="qwen2.5:0.5b", 
)

vectorestore = Chroma.from_documents(documents=splits, 
                                     embedding=embeddings)
