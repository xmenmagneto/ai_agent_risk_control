from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from tools.toolkit import tools

load_dotenv()

llm = ChatOpenAI(
    temperature=0,
    model="gpt-3.5-turbo-1106"
)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)

def run_tool_agent(message: str):
    return agent.invoke(message)