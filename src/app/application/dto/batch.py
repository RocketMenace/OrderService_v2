from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True, slots=True, kw_only=True)
class BatchDTO:
    sku: str
    qty: int
    eta: date
