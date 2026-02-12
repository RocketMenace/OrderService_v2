from datetime import date
from typing import TypedDict

from app.domain.value_objects import BatchID


class BatchContract(TypedDict):
    reference: BatchID
    sku: str
    qty: int
    eta: date | None
