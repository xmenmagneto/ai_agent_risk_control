from agents.base import BaseAgent

class ModelAgent(BaseAgent):
    async def start(self):
        pass  # 加载模型权重等

    async def stop(self):
        pass  # 资源释放

    async def process(self, input_data: dict) -> dict:
        print(f"[ModelAgent] 输入: {input_data}")

        features = input_data.get("features", {})
        print(f"[ModelAgent] 提取特征: {features}")

        score = 65  # 模拟结果
        print(f"[ModelAgent] 模拟风险评分: {score}")

        result = {"risk_score": score, **input_data}
        print(f"[ModelAgent] 输出: {result}")

        return result