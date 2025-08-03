test_data_list = [
    {
        "user_id": "black_123",  # 黑名单用户
        "features": {"f1": 0.8, "f2": 0.1}
    },
    {
        "user_id": "white_456",  # 非黑名单用户
        "features": {"f1": 0.3, "f2": 0.7}
    },
    {
        "user_id": "black_xyz",  # 黑名单用户，测试不同ID格式
        "features": {"f1": 0.5, "f2": 0.5}
    },
    {
        "user_id": "",  # user_id 为空，测试边界
        "features": {"f1": 0.1, "f2": 0.9}
    },
    {
        "user_id": "normal_user",  # 正常用户，特征全为0
        "features": {"f1": 0.0, "f2": 0.0}
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
