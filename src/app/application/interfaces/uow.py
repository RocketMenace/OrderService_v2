from typing import Protocol, Self

from app.application.interfaces.repository import (
    BatchRepositoryProtocol,
    OrderRepositoryProtocol,
)


class UnitOfWorkProtocol(Protocol):
    batches: BatchRepositoryProtocol
    orders: OrderRepositoryProtocol

    async def __aenter__(self) -> Self: ...
    async def __aexit__(self, exc_type, exc_val, exc_tb): ...
    async def commit(self) -> None: ...
    async def rollback(self) -> None: ...
