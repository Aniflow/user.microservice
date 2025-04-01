import os
from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    """Base configuration with common settings."""
    API_PORT: int = int(os.getenv("API_PORT", "8001"))
    API_HOST: str = os.getenv("API_HOST", "0.0.0.0")
    ALLOW_ORIGINS: str = os.getenv("ALLOWED_ORIGINS", "*")
    ALLOW_METHODS: str = os.getenv("ALLOWED_METHODS", "*")
    ALLOW_HEADERS: str = os.getenv("ALLOWED_HEADERS", "*")
    ALLOW_CREDENTIALS: bool = os.getenv("ALLOW_CREDENTIALS", "True").lower() in ("true", "1")  # Noqa: E501


class DevelopmentConfig(BaseConfig):
    """Configuration for development."""
    DEBUG: bool = True


class ProductionConfig(BaseConfig):
    """Configuration for production."""
    DEBUG: bool = False


ENV = os.getenv("ENV", "development").lower()
CONFIG = DevelopmentConfig() if ENV == "development" else ProductionConfig()
