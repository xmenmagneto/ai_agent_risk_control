from agents.base_agent import BaseAgent
import json
import redis.asyncio as redis

class RedisStreamAgent(BaseAgent):
    def __init__(self, name, redis_url="redis://localhost", stream_key="risk_events"):
        super().__init__(name)
        self.redis_url = redis_url
        self.stream_key = stream_key
        self.redis = None
        self.last_id = "0-0"  # 从头读起，生产环境可记录偏移

    async def start(self):
        self.redis = redis.from_url(self.redis_url)  # from_url 不再是协程，不用 await
        print(f"[{self.name}] started consuming Redis stream '{self.stream_key}'")
        while True:
            # XREAD block 0 streams key last_id
            entries = await self.redis.xread({self.stream_key: self.last_id}, block=0, count=10)
            for stream, messages in entries:
                for msg_id, msg_data in messages:
                    self.last_id = msg_id
                    data_json = msg_data[b"data"].decode()
                    event = json.loads(data_json)
                    await self.handle_message(event)

    async def handle_message(self, event):
        # 基础日志打印 + 简单预处理（示例）
        print(f"[{self.name}] received event: {event}")
        # 模拟预处理：风险分数大于0.7报警
        if event.get("risk_score", 0) > 0.7:
            print(f"[{self.name}] ALERT: High risk event detected: {event}")