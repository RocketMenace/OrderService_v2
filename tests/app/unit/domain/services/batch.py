import pytest


@pytest.mark.asyncio
async def test_prefers_current_stock_batches_to_shipments(
    make_domain_service,
    make_valid_batch_and_line,
    make_current_batch_in_shipping,
):
    service = make_domain_service
    in_stock_batch, line = make_valid_batch_and_line
    in_stock_batch.eta = None
    shipment_batch = make_current_batch_in_shipping
    await service.allocate(line=line, batches=[in_stock_batch, shipment_batch])
    assert await in_stock_batch.available_quantity == 15
    assert await shipment_batch.available_quantity == 10


@pytest.mark.asyncio
async def test_prefers_earlier_batches(
    make_domain_service,
    make_valid_batch_and_line,
    make_current_batch_in_shipping,
    make_shipping_batch_in_two_days,
):
    service = make_domain_service
    earliest_batch, line = make_valid_batch_and_line
    two_days_batch = make_shipping_batch_in_two_days
    latest_batch = make_current_batch_in_shipping
    await service.allocate(
        line=line,
        batches=[earliest_batch, two_days_batch, latest_batch],
    )
    assert await earliest_batch.available_quantity == 15
    assert await two_days_batch.available_quantity == 10
    assert await latest_batch.available_quantity == 10


@pytest.mark.asyncio
async def test_returns_allocated_batch_ref(
    make_domain_service,
    make_valid_batch_and_line,
    make_shipping_batch_in_two_days,
):
    service = make_domain_service
    in_stock_batch, line = make_valid_batch_and_line
    shipment_batch = make_shipping_batch_in_two_days
    allocation = await service.allocate(
        line=line,
        batches=[in_stock_batch, shipment_batch],
    )
    assert allocation == in_stock_batch.reference
