from agents.base import BaseAgent

class RuleAgent(BaseAgent):
    async def start(self):
        pass  # 这里可以写初始化逻辑

    async def stop(self):
        pass  # 这里可以写清理逻辑

    async def process(self, input_data: dict) -> dict:
        print(f"[RuleAgent] 输入: {input_data}")

        user_id = input_data.get("user_id", "")
        print(f"[RuleAgent] 解析 user_id: {user_id}")

        is_blacklisted = user_id.startswith("black")
        print(f"[RuleAgent] 是否黑名单命中: {is_blacklisted}")

        result = {
            **input_data,
            "rule_risk": is_blacklisted,
            "rule_reason": "黑名单命中" if is_blacklisted else "无"
        }

        print(f"[RuleAgent] 输出: {result}")
        return result



