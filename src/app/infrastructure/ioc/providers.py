from typing import AsyncGenerator

from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

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
