from typing import Literal

from dotenv import load_dotenv
from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class ApplicationSettings(BaseSettings):
    """
    Application environmental settings.
    """

    model_config = SettingsConfigDict(
        env_file=".env", env_ignore_empty=True, extra="ignore"
    )
    PROJECT_NAME: str = "spearbrain"
    DOMAIN: str = "localhost"
    API_PORT: int = 8000
    ENVIRONMENT: Literal["local", "staging", "production"] = "local"
    LOGGER_LEVEL: str | None = "INFO"

    @computed_field
    @property
    def API_URL(self) -> str:
        scheme = "http" if self.ENVIRONMENT == "local" else "https"
        return f"{scheme}://{self.DOMAIN}:{self.API_PORT}"


settings = ApplicationSettings()
