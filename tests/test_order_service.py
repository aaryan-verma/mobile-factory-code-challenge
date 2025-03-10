import pytest
from app.services.order_service import OrderService
from app.repositories.order_repository import InMemoryOrderRepository
from app.utils.constants import COMPONENTS

@pytest.fixture
def order_service():
    repository = InMemoryOrderRepository()
    return OrderService(repository=repository)

@pytest.mark.asyncio
async def test_create_order(order_service):
    """Test successful order creation."""
    components = ["A", "D", "F", "I", "K"]
    order = await order_service.create_order(components)
    
    assert order.order_id.startswith("MFC-")
    assert order.total == sum(COMPONENTS[c]["price"] for c in components)
    assert len(order.parts) == 5
    assert "LED Screen" in order.parts
    assert "Wide-Angle Camera" in order.parts

@pytest.mark.asyncio
async def test_order_persistence(order_service):
    """Test that orders are persisted in repository."""
    components = ["A", "D", "F", "I", "K"]
    order = await order_service.create_order(components)
    
    saved_order = await order_service.repository.get_by_id(order.order_id)
    assert saved_order is not None
    assert saved_order.order_id == order.order_id
    assert saved_order.total == order.total 