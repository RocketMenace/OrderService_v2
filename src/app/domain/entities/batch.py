from datetime import date
from typing import Any

from app.domain.value_objects.batch_id import BatchID
from app.domain.value_objects.order_line import OrderLine


class Batch:
    def __init__(
        self,
        *,
        reference: BatchID,
        sku: str,
        qty: int,
        eta: date | None = None,
    ):
        self.reference = reference
        self.sku = sku
        self.eta = eta
        self._purchased_quantity = qty
        self._allocations: set[OrderLine] = set()

    def __setattr__(self, key: str, value: Any) -> None:
        if key == "reference" and getattr(self, "reference", None) is not None:
            raise AttributeError("Changing entity ID is not permitted")
        object.__setattr__(self, key, value)

    async def allocate(self, *, line: OrderLine) -> None:
        if await self.can_allocate(line=line):
            self._allocations.add(line)

    async def deallocate(self, *, line: OrderLine) -> None:
        if line in self._allocations:
            self._allocations.remove(line)

    @property
    async def allocated_quantity(self) -> int:
        return sum(line.qty for line in self._allocations)

    @property
    async def available_quantity(self) -> int:
        return self._purchased_quantity - await self.allocated_quantity

    async def can_allocate(self, *, line: OrderLine) -> bool:
        return self.sku == line.sku and await self.available_quantity >= line.qty

    def __eq__(self, other):
        if not isinstance(other, Batch):
            return False
        return other.reference == self.reference

    def __hash__(self):
        return hash(self.reference)
