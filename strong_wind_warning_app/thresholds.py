def _get_kph(speed_mps):
    if speed_mps >= 0:
        speed_kmph = speed_mps * 3.6
        return speed_kmph
    else:
        raise ValueError("Input speed (m/s) must be a postive number.")


# def get_wind_status(wind_forecast: dict):

#     # {'wind_speed': 2.24, 'wind_deg': 185, 'wind_gust': 4.02}

#     speed = wind_forecast['wind_speed']
#     deg = wind_forecast['wind_deg']
#     gust = wind_forecast['wind_gust']

#     if (speed >= 3) or (gust >= 4):
