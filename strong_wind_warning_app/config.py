from pydantic import BaseSettings


class Settings(BaseSettings):
    OPEN_WEATHER_API_KEY: str  # Secret imported from env. variable
    OPEN_WEATHER_URL_BASE = "https://api.openweathermap.org/data/2.5/onecall"
    OPEN_WEATHER_API_TYPES: list[str] = [
        "current",
        "minutely",
        "hourly",
        "daily",
        "alerts",
    ]

    LOCATION_LATITUDE: str  # Secret imported from env. variable
    LOCATION_LONGITUDE: str  # Secret imported from env. variable

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
