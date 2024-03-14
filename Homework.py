class Country:
    def __init__(self, name, continent, population, phone_code, capital, cities=[]):
        self.name = name
        self.continent = continent
        self.population = population
        self.phone_code = phone_code
        self.capital = capital
        self.cities = cities

    def __str__(self):
        cities_str = ", ".join(self.cities)
        return f"Country: {self.name}\nContinent: {self.continent}\nPopulation: {self.population}\nPhone Code: {self.phone_code}\nCapital: {self.capital}\nCities: {cities_str}"

    def add_city(self, city_name):
        self.cities.append(city_name)
        print(f"Added city {city_name} to the country.")


# Example usage
country1 = Country("USA", "North America", 331000000, "1", "Washington D.C.", ["New York", "Los Angeles", "Chicago"])
print("Country Information:")
print(country1)

country1.add_city("Houston")
print("\nUpdated Country Information:")
print(country1)
