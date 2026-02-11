from typing import Generic, TypeVar

from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.persistence_sqla.models import BaseModel

ModelType = TypeVar("ModelType", bound=BaseModel)


class BaseRepository(Generic[ModelType]):
    def __init__(self, session: AsyncSession, model: type[ModelType]):
        self._session = session
        self._model = model

    async def save(self) -> ModelType:
        query = insert(self._model).values().returning(self._model)
        result = (await self._session.execute(query)).scalar_one()
        return result
