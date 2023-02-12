def forecast(*args):
    data = dict()
    weather_report = []
    for location, weather in args:
        data[location] = weather

    sort_weather = sorted(data.items(), key=lambda x: ((x[1] == "Rainy", x[1] == "Cloudy", x[1] == "Sunny"), x[0]))
    for location , weather in sort_weather:
        weather_report.append(f"{location} - {weather}")
    return "\n".join(weather_report)

