MAX_POPULATION = 5


city_list = [
    {"city": "Москва", "population": 12.5},
    {"city": "Санкт-Петербург", "population": 5.4},
    {"city": "Москва", "population": 1.6},
    {"city": "Екатеринбург", "population": 1.5},
    {"city": "Нижний Новгород", "population": 1.3},
]


def filter_population_in_list(cities_list, target):
    return len(
        [city["population"] for city in cities_list if city["population"] < target]
    )


print(
    f"Количество городов с население до 5 млн. жителей равно = {filter_population_in_list(city_list, MAX_POPULATION)}"
)
