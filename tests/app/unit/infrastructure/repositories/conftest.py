from typing import AsyncGenerator

import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.domain.entities.batch import Batch
from app.domain.value_objects import BatchID
from app.infrastructure.persistence_sqla.models import BatchModel
from app.infrastructure.persistence_sqla.repository import BatchRepository


@pytest_asyncio.fixture(scope="session")
async def get_test_session() -> AsyncGenerator[AsyncSession, None]:
    engine = create_async_engine(
        "sqlite+aiosqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=None,
    )
    session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with engine.begin() as conn:
        await conn.run_sync(BatchModel.metadata.create_all)

    async with session.begin as session:
        yield session
        await session.commit()
    await engine.dispose()


@pytest_asyncio.fixture(scope="function")
async def make_batch() -> Batch:
    return Batch(
        reference=BatchID(),
        sku="UNCOMFORTABLE-CHAIR",
        qty=10,
        eta=None,
    )


@pytest_asyncio.fixture(scope="function")
async def make_batch_repository(get_test_session):
    return BatchRepository(session=get_test_session)
