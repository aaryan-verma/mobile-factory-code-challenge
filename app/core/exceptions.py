from typing import Optional

class AppException(Exception):
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(message)

class InvalidOrderException(AppException):
    def __init__(self, message: str):
        super().__init__(message=message, status_code=400)

class OrderNotFoundException(AppException):
    def __init__(self, order_id: str):
        super().__init__(
            message=f"Order with id {order_id} not found",
            status_code=404
        ) 