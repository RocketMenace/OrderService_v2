import pytest


@pytest.mark.asyncio
async def test_save_batch_repository(
    get_test_session,
    make_batch,
    make_batch_repository,
):
    batch = make_batch
    batch_repository = make_batch_repository
    await batch_repository.save()
