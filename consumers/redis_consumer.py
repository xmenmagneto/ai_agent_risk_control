import asyncio
import redis.asyncio as redis
import json
from flows.multi_agent_graph import build_multi_agent_graph

async def redis_consumer():
    r = redis.Redis(host='localhost', port=6379, db=0)
    stream_key = "events_stream"
    group_name = "langgraph_group"
    consumer_name = "consumer_1"

    # 尝试创建消费组，若存在则忽略
    try:
        await r.xgroup_create(stream_key, group_name, id='0', mkstream=True)
    except redis.exceptions.ResponseError:
        pass

    graph = build_multi_agent_graph()

    while True:
        resp = await r.xreadgroup(group_name, consumer_name, {stream_key: ">"}, count=1, block=1000)
        if resp:
            for stream, messages in resp:
                for message_id, message in messages:
                    data_json = message[b'data'].decode()
                    event_data = json.loads(data_json)
                    print(f"[Consumer] 收到事件: {event_data}")

                    result = await graph.ainvoke(event_data)
                    print(f"[Consumer] 处理结果: {result}")

                    # 确认消息
                    await r.xack(stream_key, group_name, message_id)
        else:
            await asyncio.sleep(0.1)

if __name__ == "__main__":
    asyncio.run(redis_consumer())