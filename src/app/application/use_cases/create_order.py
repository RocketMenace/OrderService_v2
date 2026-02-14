from app.application.dto.order import OrderDTO
from app.application.interfaces import UnitOfWorkProtocol
from app.domain.services.batch import BatchService


class CreateOrderUseCase:
    def __init__(self, uow: UnitOfWorkProtocol, service: BatchService):
        self.uow = uow

    async def __call__(self, *, order: OrderDTO):
        async with self.uow:
            pass
