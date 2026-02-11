from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.persistence_sqla.models import AllocationModel
from app.infrastructure.persistence_sqla.repository import BaseRepository


class AllocationsRepository(BaseRepository[AllocationModel]):
    def __init__(self, session: AsyncSession):
        super().__init__(session=session, model=AllocationModel)
