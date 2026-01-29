from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True, slots=True, repr=False)
class OrderLine:
    order_id: str
    sku: str
    qty: int
