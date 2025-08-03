from agents.base import BaseAgent
import joblib
import numpy as np
import os

class ModelAgent(BaseAgent):
    MODEL_PATH = "models/isolation_forest.joblib"

    def __init__(self):
        if not os.path.exists(self.MODEL_PATH):
            raise FileNotFoundError(f"模型文件不存在: {self.MODEL_PATH}")
        self.model = joblib.load(self.MODEL_PATH)

    async def start(self):
        print("[ModelAgent] 模型加载完成")

    async def stop(self):
        print("[ModelAgent] 模型资源释放（如果有）")

    async def process(self, input_data: dict) -> dict:
        print(f"[ModelAgent] 输入: {input_data}")

        features_dict = input_data.get("features", {})
        feature_vector = self.extract_features(features_dict)
        print(f"[ModelAgent] 转换特征向量: {feature_vector}")

        # 传入二维数组 (1, n_features)
        raw_score = self.model.decision_function(feature_vector.reshape(1, -1))[0]
        print(f"[ModelAgent] 原始模型评分 (decision_function): {raw_score:.4f}")

        # 反转分数，越大越风险
        risk_score = -raw_score * 100

        # 简单限幅归一化，确保risk_score在0~100范围内
        risk_score = max(0, min(100, risk_score))
        print(f"[ModelAgent] 归一化后风险评分: {risk_score:.2f}")

        result = {
            **input_data,
            "risk_score": round(risk_score, 2)
        }

        print(f"[ModelAgent] 输出: {result}")
        return result

    def extract_features(self, features_dict):
        # 转成浮点型数组，顺序对应训练模型特征
        return np.array([
            features_dict.get("amount", 0),
            features_dict.get("frequency", 0),
            features_dict.get("ip_change_rate", 0),
            features_dict.get("device_change_rate", 0),
            features_dict.get("avg_session_time", 0),
            features_dict.get("region_entropy", 0)
        ], dtype=float)
