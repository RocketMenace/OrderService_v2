from datetime import datetime
from typing import TypedDict


class BatchResponse(TypedDict):
    id: str
    sku: str
    qty: int
    created_at: datetime
    updated_at: datetime
