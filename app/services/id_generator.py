from datetime import datetime
import uuid
from typing import Protocol, List
from app.utils.constants import BASE36_ALPHABET

class IdGenerator(Protocol):
    def generate(self, components: List[str]) -> str:
        ...

class OrderIdGenerator:
    PREFIX = "MFC"
    
    @classmethod
    def generate(cls) -> str:
        """Generate order ID in format: MFC-UUID-ITEMS-HASH.
        
        Example: MFC-a1b2c3d4-ADFIK-2KP5VX
        - MFC: Mobile Factory Code
        - a1b2c3d4: UUID
        - ADFIK: Component codes
        - 2KP5VX: Encoded timestamp
        """
        timestamp = int(datetime.now().timestamp())
        # Convert timestamp to base36 for shorter, readable string
        encoded_time = cls._encode_timestamp(timestamp)
        unique_id = str(uuid.uuid4())[:8]
        return f"{cls.PREFIX}-{unique_id}-{encoded_time}"
    
    @staticmethod
    def _encode_timestamp(timestamp: int) -> str:
        """Encode timestamp to base36 for shorter, readable format."""
        base36 = ''
        while timestamp:
            timestamp, i = divmod(timestamp, 36)
            base36 = BASE36_ALPHABET[i] + base36
        return base36 or '0' 