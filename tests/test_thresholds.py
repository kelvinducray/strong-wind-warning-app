from numbers import Number
from typing import Any

import pytest
from strong_wind_warning_app.thresholds import _get_kph  # , get_wind_status


# Tests for _get_kph()
@pytest.mark.parametrize(
    "input, expected",
    [(0, 0), (5, 18), (1.2334343, 4.44036348)],
)
def test_get_kph(input: Number, expected: Number) -> None:
    actual = _get_kph(input)
    assert actual == pytest.approx(expected)


@pytest.mark.parametrize(
    "input",
    [-4, -2.7853434, -3.1],
)
def test_get_kph_not_positive(input: Any):
    with pytest.raises(ValueError):
        _get_kph(input)


@pytest.mark.parametrize(
    "input",
    ["str", None, {}, []],
)
def test_get_kph_not_numeric(input: Any):
    with pytest.raises(TypeError):
        _get_kph(input)


# Tests for get_wind_status()
# @pytest.mark.parametrize(
#     "forecast, expected",
#     [
#         (input, True),
#         ("/bar", False),
#     ],
# )
# def test_get_wind_status(forecast: dict, expected: dict):
#     actual = forecast.get_wind_status()
