from fastapi import FastAPI

app = FastAPI(
    title="Enterprise Developer Portal",
    version="0.1.0",
    description="Local DevOps training platform built with FastAPI"
)

@app.get("/")
def root():
    return {"message": "Enterprise Developer Portal is running"}

@app.get("/api/health")
def health():
    return {"status": "ok"}
