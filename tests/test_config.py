from typing import Any

import pytest
from strong_wind_warning_app.config import get_settings


@pytest.mark.parametrize(
    ("deployed_env, env_name"),
    [
        # Default to Development
        (None, "Development"),
        ("DEV", "Development"),
        ("dfgdfg", "Development"),
        # Test
        ("TEST", "Test"),
        # Production
        ("PROD", "Production"),
    ],
)
def test_get_settings(deployed_env: Any, env_name: str, monkeypatch) -> None:
    if deployed_env:
        monkeypatch.setenv("DEPLOYED_ENVIRONMENT", deployed_env)

    get_settings.cache_clear()
    settings = get_settings()

    assert settings.ENVIRONMENT_NAME == env_name
