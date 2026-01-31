from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="allow",
    )

    # Project metadata
    project_name: str = Field(default="Order Service", alias="PROJECT_NAME")
    version: str = Field(default="0.1.0", alias="VERSION")
    debug: bool = Field(default=True, alias="DEBUG")

    # Application settings
    app_port: int = Field(default=8000, alias="APP_PORT")

    # Logging
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")
    log_format: str = Field(default="json")
