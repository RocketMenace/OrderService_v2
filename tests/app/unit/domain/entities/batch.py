from uuid import uuid4

import pytest

from app.domain.value_objects.order_line import OrderLine
from tests.app.unit.domain.entities.conftest import make_valid_batch_and_line


@pytest.mark.asyncio
async def test_can_allocate_if_available_greater_than_required(
    make_valid_batch_and_line,
):
    large_batch, small_line = make_valid_batch_and_line
    assert await large_batch.can_allocate(line=small_line)


@pytest.mark.asyncio
async def test_cannot_allocate_if_available_smaller_than_required(
    make_insufficient_batch,
):
    small_batch, large_line = make_insufficient_batch
    assert await small_batch.can_allocate(line=large_line) is False


@pytest.mark.asyncio
async def test_can_allocate_if_available_equal_to_required(make_equal_batch_and_line):
    batch, line = make_equal_batch_and_line
    assert await batch.can_allocate(line=line)


@pytest.mark.asyncio
async def test_cannot_allocate_if_skus_do_not_match(make_incompatible_order):
    batch, line = make_incompatible_order
    assert await batch.can_allocate(line=line) is False


@pytest.mark.asyncio
async def test_can_only_deallocate_allocated_lines(make_unallocated_line):
    batch, unallocated_line = make_unallocated_line
    await batch.deallocate(line=unallocated_line)
    assert await batch.available_quantity == 10


@pytest.mark.asyncio
async def test_allocations_is_idempotent(make_valid_batch_and_line):
    batch, line = make_valid_batch_and_line
    await batch.allocate(line=line)
    await batch.allocate(line=line)
    assert await batch.available_quantity == 15


@pytest.mark.asyncio
async def test_allocate_different_lines(make_valid_batch_and_line):
    batch, line = make_valid_batch_and_line
    await batch.allocate(line=line)
    new_line = OrderLine(
        order_id="2993108d-5106-4e93-a5c6-b2557a307b80",
        sku="UNCOMFORTABLE-CHAIR",
        qty=7,
    )
    await batch.allocate(line=new_line)
    assert await batch.available_quantity == 8


@pytest.mark.asyncio
async def test_batch_read_only_reference(make_batch):
    batch = make_batch
    with pytest.raises(AttributeError):
        batch.reference = uuid4()
