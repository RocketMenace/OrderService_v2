from datetime import date

import pytest_asyncio

from app.domain.entities.batch import Batch
from app.domain.value_objects import BatchID, OrderLine


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
async def make_insufficient_batch() -> tuple[Batch, OrderLine]:
    return Batch(
        reference=BatchID(),
        sku="UNCOMFORTABLE-CHAIR",
        qty=3,
        eta=date.today(),
    ), OrderLine(
        order_id="2993108d-5106-4e93-a5c6-b2557a307b80",
        sku="UNCOMFORTABLE-CHAIR",
        qty=5,
    )


@pytest_asyncio.fixture(scope="function")
async def make_equal_batch_and_line() -> tuple[Batch, OrderLine]:
    return Batch(
        reference=BatchID(),
        sku="UNCOMFORTABLE-CHAIR",
        qty=5,
        eta=date.today(),
    ), OrderLine(
        order_id="2993108d-5106-4e93-a5c6-b2557a307b80",
        sku="UNCOMFORTABLE-CHAIR",
        qty=5,
    )


@pytest_asyncio.fixture(scope="function")
async def make_incompatible_order() -> tuple[Batch, OrderLine]:
    return Batch(
        reference=BatchID(),
        sku="UNCOMFORTABLE-CHAIR",
        qty=10,
        eta=None,
    ), OrderLine(order_id="order-123", sku="EXPENSIVE-TOASTER", qty=10)


@pytest_asyncio.fixture(scope="function")
async def make_unallocated_line() -> tuple[Batch, OrderLine]:
    return Batch(
        reference=BatchID(),
        sku="UNCOMFORTABLE-CHAIR",
        qty=10,
        eta=None,
    ), OrderLine(order_id="order-123", sku="EXPENSIVE-TOASTER", qty=10)


@pytest_asyncio.fixture(scope="function")
async def make_batch() -> Batch:
    return Batch(
        reference=BatchID(),
        sku="UNCOMFORTABLE-CHAIR",
        qty=10,
        eta=None,
    )
