from numbers import Number
from typing import Any

import pytest

from strong_wind_warning_app.thresholds import (  # , get_wind_status
    _get_direction_name, _get_kmph)


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
        (355, "Notherly"),
        (0, "Notherly"),
        (360, "Notherly"),
        (16.7, "Notherly"),
        # East
        (82, "Easterly"),
        (90, "Easterly"),
        (91.34, "Easterly"),
        # South
        (170, "Southerly"),
        (180, "Southerly"),
        (190.01, "Southerly"),
        # West
        (263, "Westerly"),
        (270, "Westerly"),
        (281.04, "Westerly"),
        # NE
        (30.02, "North Easterly"),
        (45, "North Easterly"),
        (51, "North Easterly"),
        # SE
        (130.01, "South Easterly"),
        (135, "South Easterly"),
        (141.93, "South Easterly"),
        # SW
        (209.443, "South Westerly"),
        (225, "South Westerly"),
        (231, "South Westerly"),
        # NW
        (300, "North Westerly"),
        (315, "North Westerly"),
        (322.6, "North Westerly"),
    ],
)
def test_get_direction_name(input: Number, expected: Number) -> None:
    actual = _get_direction_name(input)
    assert actual == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        # North/NE Boundary
        (22.5, "Notherly"),
        # East/NE Boundary
        (67.5, "Easterly"),
        # East/SE Boundary
        (112.5, "Easterly"),
        # South/SE Boundary
        (157.5, "Southerly"),
        # South/SW Boundary
        (202.5, "Southerly"),
        # West/SW Boundary
        (247.5, "Westerly"),
        # West/NW Boundary
        (292.5, "Westerly"),
        # North/NW Boundary
        (337.5, "Notherly"),
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
