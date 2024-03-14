class City:
    def __init__(self, name, region, country, population, postal_code, phone_code):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.postal_code = postal_code
        self.phone_code = phone_code

    def __str__(self):
        return f"City: {self.name}\nRegion: {self.region}\nCountry: {self.country}\nPopulation: {self.population}\nPostal Code: {self.postal_code}\nPhone Code: {self.phone_code}"

    def update_population(self, new_population):
        self.population = new_population
        print("Population updated.")


city1 = City("New York", "New York", "USA", 8623000, "10001", "212")
print("City Information:")
print(city1)

city1.update_population(9000000)
print("\nUpdated City Information:")
print(city1)
