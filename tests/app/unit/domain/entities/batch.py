import pytest

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
