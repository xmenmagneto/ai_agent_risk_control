from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class RunRequest(BaseModel):
    msg: str

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}

@app.post("/run")
async def run_endpoint(request: RunRequest):
    return {"received_msg": request.msg}
