from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, slots=True, kw_only=True)
class OrderDTO:
    order_id: UUID
    sku: str
    qty: int

    def __post_init__(self):
        if isinstance(self.order_id, UUID):
            object.__setattr__(self, "order_id", str(self.order_id))
