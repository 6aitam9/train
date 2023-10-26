city_list = [
    {"city": "Москва", "population": 12.5},
    {"city": "Санкт-Петербург", "population": 5.4},
    {"city": "Москва", "population": 1.6},
    {"city": "Екатеринбург", "population": 1.5},
    {"city": "Нижний Новгород", "population": 1.3},
]


def average_population_in_list(cities_list):
    sum_population = sum([city["population"] for city in cities_list])
    count_cities = len(city_list)
    return sum_population / count_cities


print(
    f"Среднее арифметическое населения равно = {average_population_in_list(city_list)}"
)
