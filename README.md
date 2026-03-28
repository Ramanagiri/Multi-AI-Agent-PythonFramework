# 🧠 Multi-Agent Coding Assistant (LLM-Powered)

A **pure Python multi-agent system** powered by OpenAI LLMs, featuring an **Orchestrator Agent** and specialized coding agents (Python, Java, SQL) with an **"ask-before-act" approval workflow**.

Built using **FastAPI** for scalable API deployment.

---

## 🚀 Features

* 🧠 LLM-powered orchestration (decision-making agent)
* 👨‍💻 Language-specific agents:

  * Python Agent
  * Java Agent
  * SQL Agent
* 🔁 Ask-before-act approval loop (safety layer)
* ⚡ FastAPI backend
* 📦 Modular and extensible architecture
* 📊 Structured JSON outputs (reliable responses)

---

## 🏗️ Architecture

```
User → FastAPI → Orchestrator (LLM)
                        ↓
        ┌───────────────┼───────────────┐
        ↓               ↓               ↓
   Python Agent     Java Agent     SQL Agent
      (LLM)            (LLM)           (LLM)
                        ↓
              Structured Response
                        ↓
              Ask User Approval
                        ↓
                 Final Execution
```

---

## 📁 Project Structure

```
.
├── main.py        # FastAPI entrypoint
├── agents.py      # Orchestrator + Agents
├── llm.py         # OpenAI API wrapper
├── .env           # API keys
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone <your-repo-url>
cd multi-agent-assistant
```

### 2. Create virtual environment (recommended)

```
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```
pip install fastapi uvicorn openai python-dotenv pydantic
```

---

## 🔐 Environment Variables

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Running the App

```
uvicorn main:app --reload
```

API will be available at:

```
http://127.0.0.1:8000
```

Docs (Swagger UI):

```
http://127.0.0.1:8000/docs
```

---

## 🧪 API Usage

### 1️⃣ Create Plan (Ask Phase)

**POST** `/ask`

```
{
  "query": "Write a Python function to calculate factorial"
}
```

### 🔄 Response

```
{
  "status": "approval_required",
  "plan": {
    "id": "...",
    "agent": "python",
    "reason": "...",
    "task": "...",
    "status": "pending_approval"
  }
}
```

---

### 2️⃣ Approve Execution

**POST** `/ask`

```
{
  "approve": true,
  "plan_id": "PLAN_ID_HERE"
}
```

### ✅ Response

```
{
  "status": "executed",
  "result": {
    "plan": {...},
    "output": {
      "code": "...",
      "explanation": "..."
    }
  }
}
```

---

## 🧠 LLM Engineering Principles Used

* **Role-based prompting** (expert agents)
* **Structured JSON outputs** (robust parsing)
* **Low temperature for consistency**
* **Separation of concerns**
* **Approval loop for safety**

---

## 🔄 Workflow

1. User sends query
2. Orchestrator decides best agent (LLM)
3. Plan is generated
4. User approval required
5. Selected agent executes task
6. Structured response returned

---

## 🧩 Agents

| Agent        | Responsibility            |
| ------------ | ------------------------- |
| Orchestrator | Task planning & routing   |
| Python       | Python code generation    |
| Java         | Java code generation      |
| SQL          | Database query generation |

---

## 🛡️ Safety Layer

The system enforces:

* ❗ No execution without user approval
* 🔍 Transparent planning
* 🧾 Explainable reasoning

---

## 🚀 Future Improvements

* 🔥 Multi-step task decomposition
* 🧠 Memory (context-aware agents)
* 🧪 Code execution sandbox
* 🧑‍⚖️ Critic / reviewer agent
* 🌐 Web search integration
* 💬 Chat UI (React frontend)
* 🐳 Docker deployment

---

## 📌 Example Use Cases

* Code generation assistant
* Backend API builder
* SQL query generator
* Multi-language coding helper
* AI development copilots

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## 📜 License

MIT License

---

## 💡 Inspiration

Inspired by modern multi-agent systems and LLM orchestration patterns used in advanced AI assistants.

---
