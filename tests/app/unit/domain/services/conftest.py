from datetime import date, timedelta

import pytest_asyncio

from app.domain.entities.batch import Batch
from app.domain.services.batch import BatchService
from app.domain.value_objects import BatchID, OrderLine


@pytest_asyncio.fixture(scope="function")
async def make_domain_service() -> BatchService:
    return BatchService()


@pytest_asyncio.fixture(scope="function")
async def make_valid_batch_and_line() -> tuple[Batch, OrderLine]:
    return Batch(
        reference=BatchID(),
        sku="UNCOMFORTABLE-CHAIR",
        qty=20,
        eta=date.today(),
    ), OrderLine(
        order_id="2993108d-5106-4e93-a5c6-b2557a307b80",
        sku="UNCOMFORTABLE-CHAIR",
        qty=5,
    )


@pytest_asyncio.fixture(scope="function")
async def make_current_batch_in_shipping() -> Batch:
    return Batch(
        reference=BatchID(),
        sku="UNCOMFORTABLE-CHAIR",
        qty=10,
        eta=date.today() + timedelta(days=5),
    )


@pytest_asyncio.fixture(scope="function")
async def make_shipping_batch_in_two_days() -> Batch:
    return Batch(
        reference=BatchID(),
        sku="UNCOMFORTABLE-CHAIR",
        qty=10,
        eta=date.today() + timedelta(days=2),
    )
