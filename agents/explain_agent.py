from agents.base import BaseAgent

class ExplainAgent(BaseAgent):
    async def start(self):
        pass  # 初始化模型或API客户端

    async def stop(self):
        pass

    async def process(self, input_data: dict) -> dict:
        print(f"[ExplainAgent] 输入: {input_data}")

        score = input_data.get("risk_score", 0)
        rule_hit = input_data.get("rule_risk", False)

        parts = []
        if rule_hit:
            parts.append("规则判断为高风险（黑名单命中）")
        if score > 70:
            parts.append(f"模型评分为 {score}，风险较高")
        else:
            parts.append(f"模型评分为 {score}，风险较低")

        explanation = "；".join(parts)
        print(f"[ExplainAgent] 生成解释: {explanation}")

        result = {
            **input_data,
            "explanation": explanation
        }
        print(f"[ExplainAgent] 输出: {result}")
        return result
