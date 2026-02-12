from dataclasses import dataclass

from app.domain.entities.batch import Batch
from app.domain.value_objects import BatchID
from app.infrastructure.persistence_sqla.mappers.contracts import BatchContract
from app.infrastructure.persistence_sqla.models import BatchModel


@dataclass(frozen=True, slots=True)
class BatchDatabaseMapper:
    @staticmethod
    async def to_model(*, entity: Batch) -> BatchModel:
        return BatchModel(
            reference=entity.reference,
            sku=entity.sku,
            qty=await entity.available_quantity,
            eta=entity.eta,
        )

    @staticmethod
    async def to_entity(*, model: BatchModel) -> Batch:
        return Batch(
            reference=BatchID(value=str(model.reference)),
            sku=model.sku,
            qty=model.qty,
            eta=model.eta,
        )

    @staticmethod
    async def entity_to_dict(*, entity: Batch) -> BatchContract:
        return BatchContract(
            reference=entity.reference,
            sku=entity.sku,
            qty=await entity.available_quantity,
            eta=entity.eta,
        )
