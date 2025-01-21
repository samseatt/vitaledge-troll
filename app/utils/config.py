from pydantic_settings import BaseSettings
from pydantic import Field


class Config(BaseSettings):
    """
    Configuration settings for the VitalEdge Troll project.

    Environment variables can be overridden using a `.env` file or system-wide settings.
    """

    # Database configuration
    DATABASE_URL: str = Field(..., description="The database connection URL.")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Instantiate the configuration
config = Config()
