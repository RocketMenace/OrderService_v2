from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.persistence_sqla.models import OrderLineModel
from app.infrastructure.persistence_sqla.repository import BaseRepository


class OrderLineRepository(BaseRepository[OrderLineModel]):
    def __init__(self, session: AsyncSession):
        super().__init__(session=session, model=OrderLineModel)
