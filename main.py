from fastapi import FastAPI

app = FastAPI(title="Real-time Threat Detection Agent")

@app.get("/")
async def root():
    return {"message": "System Operational"}
