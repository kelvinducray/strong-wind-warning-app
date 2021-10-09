from numbers import Number
from typing import Any

import pytest
from strong_wind_warning_app.thresholds import (  # , get_wind_status
    _get_direction_name,
    _get_kmph,
)


# Tests for _get_kph()
@pytest.mark.parametrize(
    "input, expected",
    [(0, 0), (5, 18), (1.2334343, 4.44036348)],
)
def test_get_kph(input: Number, expected: Number) -> None:
    actual = _get_kmph(input)
    assert actual == pytest.approx(expected)


@pytest.mark.parametrize(
    "input",
    [-4, -2.7853434, -3.1],
)
def test_get_kph_not_positive(input: Any) -> None:
    with pytest.raises(ValueError):
        _get_kmph(input)


@pytest.mark.parametrize(
    "input",
    ["str", None, {}, []],
)
def test_get_kph_not_numeric(input: Any) -> None:
    with pytest.raises(TypeError):
        _get_kmph(input)


# Tests for _get_direction_name()
@pytest.mark.parametrize(
    "input, expected",
    [
        # North
        (355, "N"),
        (0, "N"),
        (360, "N"),
        (16.7, "N"),
        # East
        (82, "E"),
        (90, "E"),
        (91.34, "E"),
        # South
        (170, "S"),
        (180, "S"),
        (190.01, "S"),
        # West
        (263, "W"),
        (270, "W"),
        (281.04, "W"),
        # NE
        (30.02, "NE"),
        (45, "NE"),
        (51, "NE"),
        # SE
        (130.01, "SE"),
        (135, "SE"),
        (141.93, "SE"),
        # SW
        (209.443, "SW"),
        (225, "SW"),
        (231, "SW"),
        # NW
        (300, "NW"),
        (315, "NW"),
        (322.6, "NW"),
    ],
)
def test_get_direction_name(input: Number, expected: Number) -> None:
    actual = _get_direction_name(input)
    assert actual == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        # North/NE Boundary
        (22.5, "N"),
        # East/NE Boundary
        (67.5, "E"),
        # East/SE Boundary
        (112.5, "E"),
        # South/SE Boundary
        (157.5, "S"),
        # South/SW Boundary
        (202.5, "S"),
        # West/SW Boundary
        (247.5, "W"),
        # West/NW Boundary
        (292.5, "W"),
        # North/NW Boundary
        (337.5, "N"),
    ],
)
def test_get_direction_name_on_boundaries(
    input: Number,
    expected: str,
) -> None:
    actual = _get_direction_name(input)
    assert actual == expected


@pytest.mark.parametrize(
    "input",
    [-100, -0.0001, 360.0001, 720],
)
def test_get_get_direction_name_range(input: int) -> None:
    with pytest.raises(ValueError):
        _get_direction_name(input)


@pytest.mark.parametrize(
    "input",
    ["str", None, {}, []],
)
def test_get_direction_name_not_numeric(input: Any) -> None:
    with pytest.raises(TypeError):
        _get_direction_name(input)


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
