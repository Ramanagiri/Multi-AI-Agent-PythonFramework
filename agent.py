import uuid
import json
from llm import call_llm


# -------- Base Agent --------
class BaseAgent:
    def __init__(self, role):
        self.role = role

    def run(self, task: str):
        raise NotImplementedError


# -------- Python Agent --------
class PythonAgent(BaseAgent):
    def __init__(self):
        super().__init__("Expert Python Developer")

    def run(self, task: str):
        system_prompt = f"""
You are an {self.role}.
Return STRICT JSON:
{{
  "code": "...",
  "explanation": "..."
}}
"""

        output = call_llm(system_prompt, task)
        return json.loads(output)


# -------- Java Agent --------
class JavaAgent(BaseAgent):
    def __init__(self):
        super().__init__("Expert Java Developer")

    def run(self, task: str):
        system_prompt = f"""
You are an {self.role}.
Return STRICT JSON:
{{
  "code": "...",
  "explanation": "..."
}}
"""
        output = call_llm(system_prompt, task)
        return json.loads(output)


# -------- SQL Agent --------
class SQLAgent(BaseAgent):
    def __init__(self):
        super().__init__("Expert SQL Engineer")

    def run(self, task: str):
        system_prompt = f"""
You are an {self.role}.
Return STRICT JSON:
{{
  "code": "...",
  "explanation": "..."
}}
"""
        output = call_llm(system_prompt, task)
        return json.loads(output)


# -------- Orchestrator --------
class Orchestrator:
    def __init__(self):
        self.agents = {
            "python": PythonAgent(),
            "java": JavaAgent(),
            "sql": SQLAgent()
        }
        self.plans = {}

    def plan_with_llm(self, query: str):
        system_prompt = """
You are an AI orchestrator.
Decide which agent to use: python, java, or sql.

Return STRICT JSON:
{
  "agent": "python|java|sql",
  "reason": "..."
}
"""
        result = call_llm(system_prompt, query)
        return json.loads(result)

    def create_plan(self, query: str):
        decision = self.plan_with_llm(query)

        plan_id = str(uuid.uuid4())

        plan = {
            "id": plan_id,
            "agent": decision["agent"],
            "reason": decision["reason"],
            "task": query,
            "status": "pending_approval"
        }

        self.plans[plan_id] = plan
        return plan

    def execute_plan(self, plan_id: str):
        plan = self.plans.get(plan_id)

        if not plan:
            return {"error": "Invalid plan_id"}

        agent = self.agents[plan["agent"]]
        result = agent.run(plan["task"])

        return {
            "plan": plan,
            "output": result
        }
