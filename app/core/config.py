from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class ApplicationSettings(BaseSettings):
    """
    Application environmental settings.
    """

    model_config = SettingsConfigDict(
        env_file=".env", env_ignore_empty=True, extra="ignore"
    )

    LOGGER_LEVEL: str | None = "INFO"
    OPEN_AI_API_KEY: str | None = "OPEN_AI_API_KEY"
    WTOC_API_KEY: str | None = "API-KEY"
    WTOC_API_URL: str | None = "http://localhost:3000"

    TASK_QUEUE: str | None = "wtoc-tasks"

    REDIS_PASSWORD: str | None = "password"
    REDIS_SERVER: str | None = "localhost"
    REDIS_PORT: int | None = 6379

    GOOGLE_SEARCH_API_KEY: str | None = "GOOGLE-SEARCH-API-KEY"
    GOOGLE_SEARCH_ENGINE_ID: str | None = "GOOGLE-SEARCH-ENGINE-ID"
