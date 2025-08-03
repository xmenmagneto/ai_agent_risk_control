# agents/example_agent.py

from agents.base_agent import BaseAgent
import asyncio

class ExampleAgent(BaseAgent):
    async def handle_message(self, message):
        print(f"[{self.name}] processing message: {message}")
        # 模拟耗时处理
        await asyncio.sleep(1)
        print(f"[{self.name}] done processing: {message}")
