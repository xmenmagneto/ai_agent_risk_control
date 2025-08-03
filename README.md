# AI Agent 风控系统

一个基于多智能体架构的实时风控 AI Agent 项目，集成 LangGraph 流程编排，支持实时数据流接入、风控模型推理与多Agent协同。

---

## 项目亮点

- FastAPI 构建高性能异步服务
- 多Agent异步消息通信框架
- 集成 Redis Streams 进行实时数据流处理
- 支持风控模型在线推理与自适应更新
- 使用 LangGraph 实现流程编排与状态管理
- 支持插件式功能扩展和内存管理
- 容器化部署与Kubernetes高可用支持

---

## 快速开始

1. 克隆仓库  
   `git clone https://github.com/xmenmagneto/ai_agent_risk_control.git`  
   `cd ai_agent_risk_control`  

2. 安装依赖  
   `python -m venv venv`  
   `.\venv\Scripts\activate  # Windows PowerShell`  
   `pip install -r requirements.txt`  

3. 配置环境变量  
   在项目根目录创建 `.env` 文件，内容示例：  
   `OPENAI_API_KEY=你的API密钥（可选）`  
   `REDIS_URL=redis://localhost:6379`  

4. 启动服务  
   `python -m uvicorn main:app --reload`  

5. 访问接口  
   - GET `http://127.0.0.1:8000/` 返回服务状态  
   - POST `http://127.0.0.1:8000/run` 发送示例请求测试  

---

## 后续计划

- 集成多源实时风控数据流（Kafka/Redis Streams）  
- 开发风控模型Agent，支持模型推理与在线学习  
- 实现多Agent协同规则引擎，动态合成风险评分  
- 引入告警系统和日志监控，提升系统可观测性  
- 完善容器化与自动化部署，支持生产环境弹性扩展