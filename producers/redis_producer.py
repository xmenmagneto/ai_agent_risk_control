import asyncio
import redis.asyncio as redis
import json
import random
import time

REDIS_STREAM_KEY = "risk_events"

async def produce_risk_events():
    redis_client = redis.from_url("redis://localhost")
    event_id = 0
    while True:
        event = {
            "event_id": event_id,
            "user_id": random.randint(1000, 2000),
            "event_type": random.choice(["login", "transaction", "password_change"]),
            "timestamp": int(time.time()),
            "risk_score": round(random.uniform(0, 1), 3)
        }
        # XADD risk_events * key value ...
        await redis_client.xadd(REDIS_STREAM_KEY, {"data": json.dumps(event)})
        print(f"[Producer] Produced event: {event}")
        event_id += 1
        await asyncio.sleep(1)