from abc import ABC, abstractmethod
from typing import Dict, List, Optional
from app.models.order import OrderResponse

class OrderRepository(ABC):
    @abstractmethod
    async def create(self, order: OrderResponse) -> OrderResponse:
        pass
    
    @abstractmethod
    async def get_by_id(self, order_id: str) -> Optional[OrderResponse]:
        pass

class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self.orders: Dict[str, OrderResponse] = {}
    
    async def create(self, order: OrderResponse) -> OrderResponse:
        self.orders[order.order_id] = order
        return order
    
    async def get_by_id(self, order_id: str) -> Optional[OrderResponse]:
        return self.orders.get(order_id) 