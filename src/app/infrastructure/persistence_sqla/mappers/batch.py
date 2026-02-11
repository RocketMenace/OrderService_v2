from dataclasses import dataclass

from app.domain.entities.batch import Batch
from app.domain.value_objects import BatchID
from app.infrastructure.persistence_sqla.models import BatchModel


@dataclass(frozen=True, slots=True)
class BatchDatabaseMapper:
    @staticmethod
    async def to_model(*, entity: Batch) -> BatchModel:
        return BatchModel(
            reference=entity.reference,
            sku=entity.sku,
            qty=entity.available_quantity,
            eta=entity.eta,
        )

    @staticmethod
    async def to_entity(*, model: BatchModel) -> Batch:
        return Batch(
            reference=BatchID(model.reference),
            sku=model.sku,
            qty=model.qty,
            eta=model.eta,
        )
