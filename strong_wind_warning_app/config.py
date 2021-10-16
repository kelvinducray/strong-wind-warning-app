import os
from functools import lru_cache
from typing import Union

from pydantic import BaseSettings


class DevelopmentSettings(BaseSettings):
    ENVIRONMENT_NAME: str = "Development"

    OPEN_WEATHER_API_KEY: str = ""  # Secret imported from env. variable
    OPEN_WEATHER_URL_BASE: str = "https://api.openweathermap.org/data/2.5/onecall"
    OPEN_WEATHER_API_TYPES: list[str] = [
        "current",
        "minutely",
        "hourly",
        "daily",
        "alerts",
    ]

    LOCATION_LATITUDE: float = 0.0  # Secret imported from env. variable
    LOCATION_LONGITUDE: float = 0.0  # Secret imported from env. variable

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class TestSettings(DevelopmentSettings):
    ENVIRONMENT_NAME: str = "Test"


class ProductionSettings(DevelopmentSettings):
    ENVIRONMENT_NAME: str = "Production"


# Create a type for type checking
Settings = Union[DevelopmentSettings, TestSettings, ProductionSettings]


@lru_cache()
def get_settings() -> Settings:
    deployed_env = os.getenv("DEPLOYED_ENVIRONMENT")
    if deployed_env == "PROD":
        return ProductionSettings()
    elif deployed_env == "TEST":
        return TestSettings()
    else:
        return DevelopmentSettings()
