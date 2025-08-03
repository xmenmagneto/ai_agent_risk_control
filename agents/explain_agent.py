from agents.base import BaseAgent

class ExplainAgent(BaseAgent):
    async def start(self):
        print("[ExplainAgent] 启动完成")

    async def stop(self):
        print("[ExplainAgent] 已停止")

    async def process(self, input_data: dict) -> dict:
        print("="*50)
        print(f"[ExplainAgent] 接收到输入: {input_data}")

        score = input_data.get("risk_score", 0)
        rule_hit = input_data.get("rule_risk", False)

        print(f"[ExplainAgent] 风控规则命中情况: {rule_hit}")
        print(f"[ExplainAgent] 模型风险评分: {score}")

        explanation_parts = []
        if rule_hit:
            explanation_parts.append("规则判断为高风险（黑名单命中）")

        # 细化风险评分解释
        if score > 70:
            explanation_parts.append("模型评分高，风险较高")
        elif score > 30:
            explanation_parts.append("模型评分中等，风险一般")
        else:
            explanation_parts.append("模型评分低，风险较低")

        explanation = "；".join(explanation_parts)
        print(f"[ExplainAgent] 综合生成解释: {explanation}")

        result = {
            **input_data,
            "explanation": explanation
        }

        print(f"[ExplainAgent] 输出结果: {result}")
        print("="*50)
        return result
