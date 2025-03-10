from fastapi import FastAPI, Depends, HTTPException, status, Request
from app.api.routes import router
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Mobile Factory API",
    description="API for creating mobile phone orders",
    version="1.0.0"
)

# Remove the middleware that's causing issues
# We'll let the verify_credentials function handle authentication

app.include_router(router, prefix="/api/v1")

# Add an exception handler for 401 errors to ensure consistent responses
@app.exception_handler(status.HTTP_401_UNAUTHORIZED)
async def unauthorized_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={"detail": exc.detail},
        headers={"WWW-Authenticate": "Basic"},
    ) 