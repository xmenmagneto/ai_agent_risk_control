from fastapi import FastAPI
from pydantic import BaseModel
from flows.tool_graph import run_tool_agent
from fastapi.responses import JSONResponse

app = FastAPI()

class RequestMsg(BaseModel):
    msg: str

@app.post("/run")
async def run(request: RequestMsg):
    try:
        result = run_tool_agent(request.msg)
        return JSONResponse(content={"result": result}, media_type="application/json; charset=utf-8")
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, media_type="application/json; charset=utf-8")

