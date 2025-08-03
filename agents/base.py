# agents/base.py
from abc import ABC, abstractmethod

class BaseAgent(ABC):
    @abstractmethod
    async def start(self):
        pass

    @abstractmethod
    async def stop(self):
        pass

    @abstractmethod
    async def process(self, input_data: dict) -> dict:
        pass
