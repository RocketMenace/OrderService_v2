from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class OrderBaseSchema(BaseModel):
    order_id: UUID = Field(
        ...,
        description="Order UUID",
        examples=[
            "fd57c632-327c-47fe-91f2-6df7db1c5d8e",
        ],
    )
    sku: str = Field(
        ...,
        description="Stock keeping unit",
        examples=[
            "EXPENSIVE-TOASTER",
        ],
    )
    qty: int = Field(
        default=1,
        description="Item quantity",
        ge=1,
        examples=[
            1,
        ],
    )
    model_config = ConfigDict(from_attributes=True, validate_by_name=True, frozen=True)


class OrderRequestSchema(OrderBaseSchema):
    pass


class OrderResponseSchema(OrderBaseSchema):
    created_at: datetime = Field(
        ...,
        description="Order created at time",
        frozen=True,
        examples=[
            "2025-10-31T14:12:57.868385+00:00",
        ],
    )
    updated_at: datetime = Field(
        ...,
        description="Order updated at time",
        examples=[
            "2025-10-31T14:12:57.868385+00:00",
        ],
    )
