from weather_api_service import Weather


def format_weather(weather: Weather) -> str:
    """Formars weather data in string"""
    return (f"{weather.city}, Температура {weather.temperature}\N{DEGREE SIGN}C, "
            f"{weather.weather_type.value}\n"
            f"Восход: {weather.sunrise.strftime('%H:%M')}\n"
            f"Закат: {weather.sunset.strftime('%H:%M')}\n")
