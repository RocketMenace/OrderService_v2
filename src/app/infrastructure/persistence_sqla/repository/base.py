from typing import Generic, TypeVar

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.persistence_sqla.models import BaseModel

ModelType = TypeVar("ModelType", bound=BaseModel)
EntityType = TypeVar("EntityType")


class BaseRepository(Generic[ModelType]):
    def __init__(self, *, session: AsyncSession, model: type[ModelType]):
        self._session = session
        self._model = model
