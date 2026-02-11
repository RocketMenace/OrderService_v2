from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.persistence_sqla.models import BatchModel
from app.infrastructure.persistence_sqla.repository import BaseRepository


class BatchRepository(BaseRepository[BatchModel]):
    def __init__(self, session: AsyncSession):
        super().__init__(session=session, model=BatchModel)
