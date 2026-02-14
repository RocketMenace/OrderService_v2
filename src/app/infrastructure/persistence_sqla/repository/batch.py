from typing import Sequence

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.entities.batch import Batch
from app.infrastructure.persistence_sqla.mappers import BatchDatabaseMapper
from app.infrastructure.persistence_sqla.models import BatchModel
from app.infrastructure.persistence_sqla.repository import BaseRepository


class BatchRepository(BaseRepository[BatchModel]):
    def __init__(self, session: AsyncSession, mapper: BatchDatabaseMapper):
        self.mapper = mapper
        super().__init__(session=session, model=BatchModel)

    async def save(self, *, entity: Batch) -> Batch:
        data = await self.mapper.entity_to_dict(entity=entity)
        query = insert(self._model).values(**data).returning(self._model)
        result = (await self._session.execute(query)).scalar_one()
        return await self.mapper.to_entity(model=result)

    async def get_all(self) -> list[Batch]:
        query = select(self._model)
        result = (await self._session.execute(query)).scalars().all()
        return [await self.mapper.to_entity(model=model) for model in result]
