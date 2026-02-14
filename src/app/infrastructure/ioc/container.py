from dishka import make_async_container

from app.infrastructure.ioc import (
    AppSettingProvider,
    BatchMapperProvider,
    BatchRepositoryProvider,
    DatabaseSessionProvider,
)

container = make_async_container(
    DatabaseSessionProvider(),
    AppSettingProvider(),
    BatchRepositoryProvider(),
    BatchMapperProvider(),
)
