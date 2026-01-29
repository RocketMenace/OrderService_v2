from datetime import date

from app.domain.value_objects.order_line import OrderLine


class Batch:
    def __init__(self, *, reference: str, sku: str, qty: int, eta: date | None = None):
        self.reference = reference
        self.sku = sku
        self.eta = eta
        self.available_qty = qty

    async def allocate(self, *, line: OrderLine) -> None:
        self.available_qty -= line.qty

    async def can_allocate(self, *, line: OrderLine) -> bool:
        return self.sku == line.sku and self.available_qty >= line.qty
