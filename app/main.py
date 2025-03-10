from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Mobile Factory API", version="1.0")

app.include_router(router)

# Run using: uvicorn app.main:app --reload
