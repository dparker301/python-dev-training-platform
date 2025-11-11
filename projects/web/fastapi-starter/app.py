from fastapi import FastAPI
app = FastAPI(title="FastAPI Starter")
@app.get("/api/health")
async def health():
    return {"status":"ok"}
@app.get("/api/echo/{name}")
async def echo(name: str):
    return {"message": f"Hello, {name}!"}
