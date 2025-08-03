# flows/basic_graph.py
from pydantic import BaseModel
from langgraph.graph import StateGraph, END
from agents.echo_agent import EchoAgent

class EchoState(BaseModel):
    msg: str

async def echo_node(state):
    agent = EchoAgent()
    await agent.start()
    result = await agent.process(state)
    await agent.stop()
    return result

def build_graph():
    builder = StateGraph(state_schema=EchoState)  # 初始化状态图，声明传入的是 dict 类型的状态
    builder.add_node("echo", echo_node)    # 添加一个节点，命名为 "echo"
    builder.set_entry_point("echo")        # 设置图的入口为这个节点
    builder.set_finish_point("echo")       # 设置图的终点也为这个节点
    return builder.compile()               # 编译图，返回一个可运行的流程对象
