# agents/echo_agent.py
from agents.base import BaseAgent


class EchoAgent(BaseAgent):
    async def start(self):
        print("EchoAgent started")

    async def stop(self):
        print("EchoAgent stopped")

    async def process(self, input_data: dict) -> dict:
        print(f"EchoAgent received: {input_data}")
        return {"echo": input_data}