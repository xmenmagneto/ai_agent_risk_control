# agents/explain_llm_agent.py
from agents.base import BaseAgent
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class ExplainLLMAgent(BaseAgent):
    def __init__(self):
        # 读取并加载 prompt 模板，注意模板路径相对于执行目录
        template_text = Path("prompts/explain_prompt.txt").read_text(encoding="utf-8")

        self.llm = ChatOpenAI(temperature=0.3)
        self.prompt = PromptTemplate(
            template=template_text,
            input_variables=[
                "user_id", "risk_score", "rule_risk",
                "amount", "frequency", "ip_change_rate",
                "device_change_rate", "avg_session_time", "region_entropy"
            ]
        )
        # 构建链：PromptTemplate -> LLM -> 输出解析器
        self.chain = self.prompt | self.llm | StrOutputParser()

    async def start(self):
        print("[ExplainLLMAgent] LLM 模块启动完成")

    async def stop(self):
        print("[ExplainLLMAgent] 已停止")

    async def process(self, input_data: dict) -> dict:
        print(f"[ExplainLLMAgent] 接收到输入: {input_data}")

        features = input_data.get("features", {})
        inputs = {
            "user_id": input_data.get("user_id", "N/A"),
            "risk_score": input_data.get("risk_score", 0),
            "rule_risk": input_data.get("rule_risk", False),
            "amount": features.get("amount", 0),
            "frequency": features.get("frequency", 0),
            "ip_change_rate": features.get("ip_change_rate", 0),
            "device_change_rate": features.get("device_change_rate", 0),
            "avg_session_time": features.get("avg_session_time", 0),
            "region_entropy": features.get("region_entropy", 0),
        }

        explanation = self.chain.invoke(inputs)
        print(f"[ExplainLLMAgent] 生成解释: {explanation}")

        return {
            **input_data,
            "explanation": explanation
        }
