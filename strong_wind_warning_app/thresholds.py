from numbers import Number


def _get_kmph(speed_mps: Number):
    """
    Converts speeds from metres/second to kilometers per hour.
    """

    if speed_mps >= 0:
        speed_kmph = speed_mps * 3.6
        return speed_kmph
    else:
        raise ValueError("Input speed (m/s) must be a postive number.")


def _get_direction_name(deg: Number):
    """
    Note: In this implementation on the borderlines of NE, SE, SW, & NW, the
    respective N, E, S, W direction will be prioritised.

    E.g. If the angle is precisely 22.5 degrees (the boundary between N & NE),
    N will be preferentially chosen.
    """

    # Check validity of angle first
    if (deg <= 360) and (deg >= 0):
        # North
        if (deg >= 337.5) or (deg <= 22.5):
            return "Notherly"
        # East
        elif (deg >= 67.5) and (deg <= 112.5):
            return "Easterly"
        # South
        elif (deg >= 157.5) and (deg <= 202.5):
            return "Southerly"
        # West
        elif (deg >= 247.5) and (deg <= 292.5):
            return "Westerly"
        # NE
        elif (deg > 22.5) and (deg < 67.5):
            return "North Easterly"
        # SE
        elif (deg > 112.5) and (deg < 157.7):
            return "South Easterly"
        # SW
        elif (deg > 202.5) and (deg < 247.5):
            return "South Westerly"
        # NW
        elif (deg > 292.5) and (deg < 337.5):
            return "North Westerly"
    else:
        raise ValueError("Input degrees must be a between 0 and 360.")


def get_wind_status(wind_forecast: dict):

    """
    This function ingests the filtered response from the weather API and
    determines the wind risk. It returns a dictionary with a status message,
    what the wind forecast is and free text to paddlers advising what to do
    given the forecast data.

    Input dictionary format example:
    {
        'wind_speed': 2.24,
        'wind_deg': 185,
        'wind_gust': 4.02
    }

    Where the wind speeds are expressed in metres/second and the angle is the
    direction where the wind is coming from (North being zero degrees and the
    angles increading in the clockwise direction).
    """

    speed = _get_kmph(wind_forecast["wind_speed"])
    gust = _get_kmph(wind_forecast["wind_gust"])
    direction = _get_direction_name(wind_forecast["wind_deg"])

    # Caution warning
    if (speed >= 30) or (gust >= 40):
        return {
            "status": "Caution",
            "wind_forecast": ("" ""),
            "message": (
                f"Strong {direction} winds. In-experienced paddlers please "
                "consider cancelling your session. Experienced paddlers "
                "please exercise extreme caution."
            ),
        }
    # Cancel classes
    elif (speed >= 40) or (gust >= 50):
        return {
            "status": "Hazardous condtions",
            "wind_forecast": ("" ""),
            "message": (
                f"Very strong {direction} winds. All paddlers please cancel "
                "your session today."
            ),
        }
    # No warnings
    else:
        return {
            "status": "No current warnings",
            "wind_forecast": ("" ""),
            "message": (
                "No current wind warnings, however please still paddle with "
                "caution and stick together."
            ),
        }
