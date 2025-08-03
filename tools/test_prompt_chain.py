from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

template_text = Path("prompts/explain_prompt.txt").read_text(encoding="utf-8")

prompt = PromptTemplate(
    template=template_text,
    input_variables=[
        "user_id", "risk_score", "rule_risk",
        "amount", "frequency", "ip_change_rate",
        "device_change_rate", "avg_session_time", "region_entropy"
    ]
)

llm = ChatOpenAI(temperature=0.3)
chain = prompt | llm | StrOutputParser()

input_data = {
    "user_id": "user_001",
    "risk_score": 82.5,
    "rule_risk": True,
    "amount": 320.0,
    "frequency": 22,
    "ip_change_rate": 0.018,
    "device_change_rate": 0.02,
    "avg_session_time": 13,
    "region_entropy": 1.6
}

result = chain.invoke(input_data)
print("解释输出：")
print(result)
