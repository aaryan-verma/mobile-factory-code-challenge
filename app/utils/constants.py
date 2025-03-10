from typing import Dict
from app.models.component import ComponentCategory

# Base36 alphabet for ID generation
BASE36_ALPHABET = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Log Messages
class LogMessage:
    # Info messages
    ORDER_CREATION_STARTED = "Creating new order with components: {}"
    ORDER_CREATED_SUCCESS = "Order created successfully: {}"
    ORDER_DETAILS = "Order details: total={}, parts={}"
    
    # Error messages
    ORDER_CREATION_FAILED = "Failed to create order: {}"
    INVALID_COMPONENTS = "Invalid components provided: {}"
    DATABASE_ERROR = "Database error occurred: {}"

# Component mapping (code -> {price, part, category})
COMPONENTS: Dict[str, Dict[str, any]] = {
    "A": {"price": 10.28, "part": "LED Screen", "category": ComponentCategory.SCREEN},
    "B": {"price": 24.07, "part": "OLED Screen", "category": ComponentCategory.SCREEN},
    "C": {"price": 33.30, "part": "AMOLED Screen", "category": ComponentCategory.SCREEN},
    "D": {"price": 25.94, "part": "Wide-Angle Camera", "category": ComponentCategory.CAMERA},
    "E": {"price": 32.39, "part": "Ultra-Wide-Angle Camera", "category": ComponentCategory.CAMERA},
    "F": {"price": 18.77, "part": "USB-C Port", "category": ComponentCategory.PORT},
    "G": {"price": 15.13, "part": "Micro-USB Port", "category": ComponentCategory.PORT},
    "H": {"price": 20.00, "part": "Lightning Port", "category": ComponentCategory.PORT},
    "I": {"price": 42.31, "part": "Android OS", "category": ComponentCategory.OS},
    "J": {"price": 45.00, "part": "iOS OS", "category": ComponentCategory.OS},
    "K": {"price": 45.00, "part": "Metallic Body", "category": ComponentCategory.BODY},
    "L": {"price": 30.00, "part": "Plastic Body", "category": ComponentCategory.BODY},
} 