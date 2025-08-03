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
    }
]

# 运行多个测试样例的示例代码：
import asyncio
from flows.multi_agent_graph import build_multi_agent_graph_using_openai

async def run_multi_agent_flow_using_openai(input_data):
    graph = build_multi_agent_graph_using_openai()
    result = await graph.ainvoke(input_data)  # 注意用异步调用
    return result

if __name__ == "__main__":
    for data in test_data_list:
        res = asyncio.run(run_multi_agent_flow_using_openai(data))
        print(f"Input: {data}")
        print(f"Output: {res}\n")
