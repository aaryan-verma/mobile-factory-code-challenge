from app.services.id_generator import OrderIdGenerator

def test_order_id_format():
    """Test that generated order ID follows the correct format."""
    order_id = OrderIdGenerator.generate()
    parts = order_id.split('-')
    
    assert len(parts) == 3
    assert parts[0] == "MFC"
    assert len(parts[1]) == 8  # UUID part
    assert len(parts[2]) > 0   # Timestamp hash

def test_unique_ids():
    """Test that generated IDs are unique."""
    ids = [OrderIdGenerator.generate() for _ in range(100)]
    assert len(set(ids)) == 100  # All IDs should be unique 