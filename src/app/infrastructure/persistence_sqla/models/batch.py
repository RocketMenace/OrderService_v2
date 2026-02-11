from datetime import date

from sqlalchemy import CheckConstraint, Date, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.persistence_sqla.models.base import BaseModel


class BatchModel(BaseModel):
    __tablename__ = "batches"
    __table_args__ = [CheckConstraint("qty > 0", name="positive_qty")]

    reference: Mapped[str] = mapped_column(String(255))
    sku: Mapped[str] = mapped_column(String(255))
    qty: Mapped[int] = mapped_column(Integer)
    eta: Mapped[date | None] = mapped_column(Date)
