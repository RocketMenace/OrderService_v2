from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.persistence_sqla.models import BaseModel, OrderModel


class OrderLineModel(BaseModel):
    __tablename__ = "order_lines"

    sku: Mapped[str] = mapped_column(String(255))
    qty: Mapped[int] = mapped_column(Integer)
    order_id: Mapped[str] = mapped_column(ForeignKey("orders.id", ondelete="CASCADE"))

    # === RELATIONSHIPS ===
    order: Mapped["OrderModel"] = relationship(
        back_populates="order",
        cascade="all, delete-orphan",
    )
