from typing import Self

from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.persistence_sqla.mappers import BatchDatabaseMapper
from app.infrastructure.persistence_sqla.repository import (
    BatchRepository,
    OrderRepository,
)


class UnitOfWork:
    def __init__(self, session: AsyncSession, batch_mapper: BatchDatabaseMapper):
        self.session = session
        self.batch_mapper = batch_mapper
        self._batches: BatchRepository | None = None
        self._orders: OrderRepository | None = None

    @property
    def batches(self) -> BatchRepository:
        if self._batches is None:
            self._batches = BatchRepository(
                session=self.session,
                mapper=self.batch_mapper,
            )
        return self._batches

    @property
    def orders(self) -> OrderRepository:
        if self._orders is None:
            self._orders = OrderRepository(session=self.session)
        return self._orders

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self.session.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
