import pytest


@pytest.mark.asyncio
async def test_map_entity_to_model(make_batch, make_batch_database_mapper):
    mapper = make_batch_database_mapper
    batch_model = await mapper.to_model(entity=make_batch)
    assert batch_model.reference == make_batch.reference
    assert batch_model.sku == make_batch.sku
    assert batch_model.eta == make_batch.eta
    assert batch_model.qty == await make_batch.available_quantity


@pytest.mark.asyncio
async def test_map_model_to_entity(make_batch_model, make_batch_database_mapper):
    mapper = make_batch_database_mapper
    batch_entity = await mapper.to_entity(model=make_batch_model)
    assert batch_entity.reference.value == str(make_batch_model.reference)
    assert batch_entity.eta == make_batch_model.eta
    assert batch_entity.sku == make_batch_model.sku
    assert await batch_entity.available_quantity == make_batch_model.qty
