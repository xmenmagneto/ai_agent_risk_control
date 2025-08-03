# train_model.py
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import joblib
import os

def generate_mock_data(n_samples=5000):
    """
    生成模拟的风控业务数据，包含多个数值特征。
    """
    amount = np.random.normal(300, 100, n_samples)               # 交易金额
    frequency = np.random.normal(20, 5, n_samples)               # 日均操作频率
    ip_change_rate = np.random.normal(0.02, 0.01, n_samples)     # IP变更频率
    device_change_rate = np.random.normal(0.03, 0.015, n_samples)# 设备变更频率
    avg_session_time = np.random.normal(15, 5, n_samples)        # 会话平均时长
    region_entropy = np.random.normal(1.5, 0.5, n_samples)       # 登录地域分散程度

    x_train = np.stack([
        amount,
        frequency,
        ip_change_rate,
        device_change_rate,
        avg_session_time,
        region_entropy
    ], axis=1)

    return x_train

def train_and_save():
    x_train = generate_mock_data(n_samples=5000)

    # 标准化处理，防止特征尺度差异影响模型
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x_train)

    # 初始化并训练 IsolationForest 模型
    model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
    model.fit(x_scaled)

    # 计算训练集样本的决策函数分数
    decision_scores = model.decision_function(x_scaled)
    min_score = decision_scores.min()
    max_score = decision_scores.max()

    # 保存模型和 scaler
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/isolation_forest.joblib")
    joblib.dump(scaler, "models/scaler.joblib")

    print("模型训练完成并保存：")
    print("  - models/isolation_forest.joblib")
    print("  - models/scaler.joblib")
    print(f"训练集决策函数分数范围：MIN_SCORE = {min_score:.6f}, MAX_SCORE = {max_score:.6f}")


if __name__ == "__main__":
    train_and_save()