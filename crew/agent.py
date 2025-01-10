import os 
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model = "qwen2.5:0.5b", 
    base_url="http://localhost:11434/v1" 
    )

os.environ["OPENAI_API_KEY"] = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

info_aget = Agent(
    role= "Information gathering",
    goal = "Find the answer to the question",
    backstory= "I am a student and I want to know the answer to the question",
    llm=llm,
    # tools=["google-search", "wikipedia-search"],
    # memory=None,
    verbose=True,
    )

task1 = Task(
    description="Tell me about India",
    expected_output="The answer to the question",
    agent=info_aget,
    )

crew = Crew(
    name="Information gathering",
    tasks=[task1],
    )

crew.run()