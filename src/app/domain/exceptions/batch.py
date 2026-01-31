from app.domain.exceptions.base import DomainError


class OutOfStockError(DomainError):
    def __init__(self, sku: str):
        message = f"Item with {sku} out of stock"
        super().__init__(message)
