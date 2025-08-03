# main.py

from fastapi import FastAPI
import asyncio
from agents.example_agent import ExampleAgent

app = FastAPI()

# 创建两个 agent 实例
agent1 = ExampleAgent("Agent-1")
agent2 = ExampleAgent("Agent-2")

@app.on_event("startup")
async def startup_event():
    # 启动两个 Agent 的事件循环
    asyncio.create_task(agent1.start())
    asyncio.create_task(agent2.start())

    # 示例：agent1 给 agent2 发消息
    await asyncio.sleep(0.5)
    await agent1.send_message(agent2, "Risk event: user login anomaly")

@app.post("/send/")
async def send_message(to_agent: str, message: str):
    if to_agent == "Agent-1":
        await agent1.queue.put(message)
    elif to_agent == "Agent-2":
        await agent2.queue.put(message)
    else:
        return {"error": "unknown agent"}
    return {"status": "message sent"}
