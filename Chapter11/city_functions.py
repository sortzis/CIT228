def city_country(city, country, population=""):
    if population:
        info = f"{city}, {country} - Population: {population}"
    else:
        info = f"{city}, {country}"
    return info.title()