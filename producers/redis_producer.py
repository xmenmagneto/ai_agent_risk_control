import asyncio
import redis.asyncio as redis
import json

async def redis_producer():
    r = redis.Redis(host='localhost', port=6379, db=0)
    stream_key = "events_stream"
    count = 0
    while True:
        data = {"user_id": f"user_{count}", "features": {"f1": count * 0.1, "f2": 0.5}}
        await r.xadd(stream_key, {"data": json.dumps(data)})
        print(f"[Producer] 写入事件: {data}")
        count += 1
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(redis_producer())