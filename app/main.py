from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router

app = FastAPI(
    title="Engineering Intelligence AI",
    description="LLM-powered system for bug analysis and failure prediction",
    version="1.0.0"
)

# ✅ CORS (allow frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "Engineering Intelligence AI System Running 🚀"}

app.include_router(router)