from app.application.interfaces import UnitOfWorkProtocol


class CreateOrderUseCase:
    def __init__(self, uow: UnitOfWorkProtocol):
        self.uow = uow

    async def __call__(self):
        async with self.uow:
            pass
