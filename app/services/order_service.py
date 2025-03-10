from typing import Dict, List
from app.utils.constants import COMPONENTS, LogMessage
from app.services.id_generator import OrderIdGenerator
from app.repositories.order_repository import OrderRepository
from app.models.order import OrderResponse
from app.core.logger import logger

class OrderService:
    def __init__(self, repository: OrderRepository):
        self.repository = repository
        
    async def create_order(self, components: List[str]) -> OrderResponse:
        """Create and store a new order."""
        logger.info(LogMessage.ORDER_CREATION_STARTED.format(components))
        
        try:
            total_price = sum(COMPONENTS[code]["price"] for code in components)
            part_names = [COMPONENTS[code]["part"] for code in components]
            order_id = OrderIdGenerator.generate()

            order = OrderResponse(
                order_id=order_id,
                total=round(total_price, 2),
                parts=part_names
            )
            
            logger.info(LogMessage.ORDER_CREATED_SUCCESS.format(order_id))
            logger.info(LogMessage.ORDER_DETAILS.format(total_price, part_names))
            
            return await self.repository.create(order)
        except Exception as e:
            logger.error(LogMessage.ORDER_CREATION_FAILED.format(str(e)))
            raise
