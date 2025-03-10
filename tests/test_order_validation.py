import pytest
from app.models.order import OrderRequest
from app.utils.constants import COMPONENTS

def test_valid_order():
    """Test that a valid order passes validation."""
    order = OrderRequest(components=["A", "D", "F", "I", "K"])
    assert order.components == ["A", "D", "F", "I", "K"]

def test_duplicate_components():
    """Test that duplicate components raise error."""
    with pytest.raises(ValueError, match="Duplicate components are not allowed"):
        OrderRequest(components=["A", "A", "F", "I", "K"])

def test_invalid_component_codes():
    """Test that invalid component codes raise error."""
    with pytest.raises(ValueError, match="Invalid component codes"):
        OrderRequest(components=["A", "X", "F", "I", "K"])

def test_duplicate_category():
    """Test that duplicate categories raise error."""
    with pytest.raises(ValueError, match="Duplicate category"):
        OrderRequest(components=["A", "B", "F", "I", "K"])  # A and B are both screens

def test_missing_category():
    """Test that missing categories raise error."""
    with pytest.raises(ValueError, match="Missing categories"):
        OrderRequest(components=["A", "D", "F", "I"])  # Missing Body 