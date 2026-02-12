from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.entities.batch import Batch
from app.infrastructure.persistence_sqla.models import OrderModel
from app.infrastructure.persistence_sqla.repository import BaseRepository


class OrderRepository(BaseRepository[OrderModel]):
    def __init__(self, session: AsyncSession):
        super().__init__(session=session, model=OrderModel)
