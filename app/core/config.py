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
    API_URL: str | None = "http://localhost:3000"
