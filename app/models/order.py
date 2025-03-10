from pydantic import BaseModel, field_validator, Field
from typing import List, Set
from app.models.component import ComponentCategory
from app.utils.constants import COMPONENTS, LogMessage
from app.core.logger import logger

class OrderRequest(BaseModel):
    components: List[str] = Field(..., description="List of component codes (A-L)")
    
    @field_validator('components')
    @classmethod
    def validate_components(cls, components):
        try:
            # Convert to set to check for duplicates
            if len(set(components)) != len(components):
                error_msg = "Duplicate components are not allowed"
                logger.error(LogMessage.INVALID_COMPONENTS.format(error_msg))
                raise ValueError(error_msg)
                
            # Validate all components are valid codes
            valid_codes = set("ABCDEFGHIJKL")
            invalid_codes = [c for c in components if c not in valid_codes]
            if invalid_codes:
                error_msg = f"Invalid component codes: {', '.join(invalid_codes)}"
                logger.error(LogMessage.INVALID_COMPONENTS.format(error_msg))
                raise ValueError(error_msg)
            
            # Validate categories
            seen_categories: Set[ComponentCategory] = set()
            for code in components:
                category = COMPONENTS[code]["category"]
                if category in seen_categories:
                    error_msg = f"Duplicate category: {category.value}"
                    logger.error(LogMessage.INVALID_COMPONENTS.format(error_msg))
                    raise ValueError(error_msg)
                seen_categories.add(category)
            
            # Check if all categories are present
            missing_categories = set(ComponentCategory) - seen_categories
            if missing_categories:
                error_msg = f"Missing categories: {', '.join(c.value for c in missing_categories)}"
                logger.error(LogMessage.INVALID_COMPONENTS.format(error_msg))
                raise ValueError(error_msg)
                
            return components
        except Exception as e:
            logger.error(LogMessage.INVALID_COMPONENTS.format(str(e)))
            raise

class OrderResponse(BaseModel):
    order_id: str
    total: float = Field(..., description="Total price of the order")
    parts: List[str] = Field(..., description="List of component names")
