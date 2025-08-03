# agents/base_agent.py

import asyncio

class BaseAgent:
    def __init__(self, name):
        self.name = name
        self.queue = asyncio.Queue()

    async def start(self):
        print(f"[{self.name}] started.")
        while True:
            message = await self.queue.get()
            await self.handle_message(message)

    async def handle_message(self, message):
        # 默认处理方式，可以被子类重写
        print(f"[{self.name}] received message: {message}")

    async def send_message(self, other_agent, message):
        await other_agent.queue.put(message)
        print(f"[{self.name}] sent message to {other_agent.name}: {message}")
