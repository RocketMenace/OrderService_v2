from typing import Protocol

from app.domain.entities.batch import Batch


class OrderRepositoryProtocol(Protocol):
    async def save(self, batch: Batch) -> None: ...
