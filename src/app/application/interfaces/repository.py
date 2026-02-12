from typing import Protocol

from app.domain.entities.batch import Batch


class OrderRepositoryProtocol(Protocol):
    async def save(self, batch: Batch) -> Batch: ...

    async def get(self): ...


class BatchRepositoryProtocol(Protocol):
    async def save(self, *, batch: Batch) -> Batch: ...

    async def get_by_reference(self, *, reference: str) -> Batch | None: ...
