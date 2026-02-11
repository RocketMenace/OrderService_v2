from app.infrastructure.persistence_sqla.models.base import BaseModel


class BatchModel(BaseModel):
    __tablename__ = "batches"
