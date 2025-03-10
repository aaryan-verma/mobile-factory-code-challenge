from app.repositories.order_repository import InMemoryOrderRepository
from app.services.order_service import OrderService

# Simple service locator pattern
order_repository = InMemoryOrderRepository()
order_service = OrderService(repository=order_repository) 