import uuid

import pytest_asyncio

from app.domain.entities.batch import Batch
from app.domain.value_objects import BatchID
from app.infrastructure.persistence_sqla.mappers import BatchDatabaseMapper
from app.infrastructure.persistence_sqla.models import BatchModel


@pytest_asyncio.fixture(scope="function")
async def make_batch() -> Batch:
    return Batch(
        reference=BatchID(),
        sku="UNCOMFORTABLE-CHAIR",
        qty=10,
        eta=None,
    )


@pytest_asyncio.fixture(scope="function")
async def make_batch_model() -> BatchModel:
    return BatchModel(
        reference=uuid.uuid4(),
        sku="UNCOMFORTABLE-CHAIR",
        qty=10,
    )


@pytest_asyncio.fixture(scope="function")
async def make_batch_database_mapper() -> BatchDatabaseMapper:
    return BatchDatabaseMapper()
