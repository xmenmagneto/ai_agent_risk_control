# 🧠 AI Agent Risk Control System

一个面向金融、风控、安全场景的智能 Agent 系统，基于 FastAPI + asyncio 构建，支持多智能体协同处理风控事件。该系统具备模块化、异步化、可扩展的架构，适用于风控评分、异常检测、用户画像等任务。

## 📦 项目亮点

- 支持多个异步智能体（Agent）并发运行  
- 每个 Agent 拥有独立消息队列（支持未来接入 Kafka / Redis 等）  
- 内置 HTTP 接口（基于 FastAPI），支持外部系统接入  
- 易于扩展：继承 `BaseAgent` 即可快速开发新模块  
- 可拓展性强，适合做微服务风控网格（Risk Micro-Mesh）

## 🏗️ 项目结构
```
ai_agent_risk_control/
├── agents/
│   ├── __init__.py
│   ├── base_agent.py         # Agent 抽象基类
│   └── example_agent.py      # 示例 Agent
├── main.py                   # FastAPI 服务入口
├── requirements.txt          # 依赖列表
└── README.md
```

## 🚀 快速开始
```
1️⃣ 克隆仓库

git clone https://github.com/yourusername/ai_agent_risk_control.git
cd ai_agent_risk_control

2️⃣ 创建虚拟环境并激活

python -m venv venv
# Windows PowerShell
.\venv\Scripts\Activate.ps1
# macOS/Linux
source venv/bin/activate

3️⃣ 安装依赖

pip install -r requirements.txt

4️⃣ 启动服务

uvicorn main:app --reload

接口文档地址：http://127.0.0.1:8000/docs
```

## 🧱 可拓展方向

- 引入大模型能力（如调用 OpenAI、文心一言、通义千问等）进行风控分析  
- 对接 Kafka 或 Redis 实现跨服务 Agent 通信  
- Agent 之间建立图结构，支持上下游依赖关系  
- 引入向量数据库，用于用户行为画像和历史模式识别  
- 增加认证与日志模块（用于生产部署）

## 📌 环境要求

- Python 3.8+
- FastAPI
- uvicorn
- asyncio