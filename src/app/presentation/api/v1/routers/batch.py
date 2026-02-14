from fastapi import APIRouter, status

from app.presentation.api.v1.schemas import OrderRequestSchema, OrderResponseSchema

router = APIRouter(prefix="/orders", tags=["v1 Orders"])


@router.post(
    "/allocate",
    response_model=OrderResponseSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_order(order: OrderRequestSchema):
    pass
