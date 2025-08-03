test_data_list = [
    {
        "user_id": "black_001",
        "features": {
            "amount": 500.0,
            "frequency": 50,
            "ip_change_rate": 0.2,
            "device_change_rate": 0.25,
            "avg_session_time": 5,
            "region_entropy": 3.2
        }
    },
    {
        "user_id": "white_002",
        "features": {
            "amount": 150.0,
            "frequency": 10,
            "ip_change_rate": 0.01,
            "device_change_rate": 0.02,
            "avg_session_time": 20,
            "region_entropy": 1.0
        }
    },
    {
        "user_id": "black_003",
        "features": {
            "amount": 800.0,
            "frequency": 100,
            "ip_change_rate": 0.5,
            "device_change_rate": 0.6,
            "avg_session_time": 3,
            "region_entropy": 4.5
        }
    },
    {
        "user_id": "",
        "features": {
            "amount": 0.0,
            "frequency": 0,
            "ip_change_rate": 0.0,
            "device_change_rate": 0.0,
            "avg_session_time": 0,
            "region_entropy": 0.0
        }
    },
    {
        "user_id": "user_normal",
        "features": {
            "amount": 220.0,
            "frequency": 15,
            "ip_change_rate": 0.015,
            "device_change_rate": 0.01,
            "avg_session_time": 18,
            "region_entropy": 1.3
        }
    }
]

# 运行多个测试样例的示例代码：
import asyncio
from flows.multi_agent_graph import build_multi_agent_graph

async def run_multi_agent_flow(input_data):
    graph = build_multi_agent_graph()
    result = await graph.ainvoke(input_data)  # 注意用异步调用
    return result

if __name__ == "__main__":
    for data in test_data_list:
        res = asyncio.run(run_multi_agent_flow(data))
        print(f"Input: {data}")
        print(f"Output: {res}\n")
