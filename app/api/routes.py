from fastapi import APIRouter, HTTPException, Depends
from app.models.order import OrderRequest, OrderResponse
from app.core.container import order_service
from app.utils.constants import LogMessage
from app.core.logger import logger
from fastapi.security import HTTPBasicCredentials
from app.core.auth import verify_credentials
import time
from datetime import datetime

router = APIRouter()

@router.post("/orders", response_model=OrderResponse, status_code=201)
async def place_order(order: OrderRequest, credentials: HTTPBasicCredentials = Depends(verify_credentials)):
    try:
        return await order_service.create_order(order.components)
    except ValueError as e:
        logger.error(LogMessage.INVALID_COMPONENTS.format(str(e)))
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(LogMessage.ORDER_CREATION_FAILED.format(str(e)))
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get("/health", status_code=200)
async def health_check():
    """
    Simple health check endpoint to verify the API is running.
    No authentication required.
    """
    return {
        "status": "ok",
        "timestamp": datetime.now().isoformat(),
        "service": "Mobile Factory API",
        "version": "1.0.0"
    }