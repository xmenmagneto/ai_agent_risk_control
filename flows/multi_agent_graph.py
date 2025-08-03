from langgraph.graph import StateGraph
from typing import TypedDict

from agents.explain_llm_agent import ExplainLLMAgent
from agents.rule_agent import RuleAgent
from agents.model_agent import ModelAgent
from agents.explain_agent import ExplainAgent

# 定义状态结构（schema），用 TypedDict 描述传递给每个节点的数据结构
class Features(TypedDict):
    amount: float
    frequency: int
    ip_change_rate: float
    device_change_rate: float
    avg_session_time: float
    region_entropy: float

class AgentState(TypedDict):
    user_id: str
    features: Features
    risk_score: float
    rule_risk: bool
    rule_reason: str
    explanation: str

# 各个异步节点函数，实例化 Agent，调用其 start/process/stop 生命周期
async def rule_node(state: dict) -> dict:
    agent = RuleAgent()
    await agent.start()
    result = await agent.process(state)
    await agent.stop()
    return result

async def model_node(state: dict) -> dict:
    agent = ModelAgent()
    await agent.start()
    result = await agent.process(state)
    await agent.stop()
    return result

async def explain_node(state: dict) -> dict:
    agent = ExplainAgent()
    await agent.start()
    result = await agent.process(state)
    await agent.stop()
    return result

async def explain_llm_node(state: dict) -> dict:
    agent = ExplainLLMAgent()
    await agent.start()
    result = await agent.process(state)
    await agent.stop()
    return result

# 构建多Agent流程图，明确执行顺序和入口、出口节点
def build_multi_agent_graph():
    builder = StateGraph(AgentState)  # 传入状态schema保证类型安全

    builder.add_node("rule", rule_node)
    builder.add_node("model", model_node)
    builder.add_node("explain", explain_node)

    builder.set_entry_point("rule")
    builder.add_edge("rule", "model")
    builder.add_edge("model", "explain")
    builder.set_finish_point("explain")

    return builder.compile()

def build_multi_agent_graph_using_openai():
    builder = StateGraph(AgentState)  # 传入状态schema保证类型安全

    builder.add_node("rule", rule_node)
    builder.add_node("model", model_node)
    builder.add_node("explain", explain_llm_node)

    builder.set_entry_point("rule")
    builder.add_edge("rule", "model")
    builder.add_edge("model", "explain")
    builder.set_finish_point("explain")

    return builder.compile()
