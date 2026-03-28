from fastapi import FastAPI
from pydantic import BaseModel
from agents import Orchestrator

app = FastAPI()
orchestrator = Orchestrator()

class Request(BaseModel):
    query: str
    approve: bool = False
    plan_id: str | None = None


@app.post("/ask")
def ask(req: Request):
    if not req.approve:
        plan = orchestrator.create_plan(req.query)
        return {
            "status": "approval_required",
            "plan": plan
        }
    else:
        result = orchestrator.execute_plan(req.plan_id)
        return {
            "status": "executed",
            "result": result
        }
