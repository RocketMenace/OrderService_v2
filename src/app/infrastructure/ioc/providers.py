from typing import AsyncGenerator

from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.persistence_sqla.mappers import BatchDatabaseMapper
from app.infrastructure.persistence_sqla.repository import (
    AllocationsRepository,
    BatchRepository,
    OrderRepository,
)
from app.setup.config import Database, Settings


class AppSettingProvider(Provider):
    scope = Scope.APP

    @provide
    async def provide_app_settings(self) -> Settings:
        return Settings()


class DatabaseSessionProvider(Provider):
    scope = Scope.REQUEST

    @provide
    async def provide_session(
        self,
        settings: Settings,
    ) -> AsyncGenerator[AsyncSession, None]:
        database = Database(url=settings.db_url)
        async with database.get_session() as session:
            yield session


class BatchMapperProvider(Provider):
    scope = Scope.REQUEST

    @provide
    async def provide_batch_mapper(self) -> BatchDatabaseMapper:
        return BatchDatabaseMapper()


class BatchRepositoryProvider(Provider):
    scope = Scope.REQUEST

    @provide
    async def provide_batch_repository(
        self,
        session: AsyncSession,
        mapper: BatchDatabaseMapper,
    ) -> BatchRepository:
        return BatchRepository(session=session, mapper=mapper)
