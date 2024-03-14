class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def __str__(self):
        return f"Stadium: {self.name}\nOpening Date: {self.opening_date}\nCountry: {self.country}\nCity: {self.city}\nCapacity: {self.capacity}"

    @classmethod
    def create_from_input(cls):
        name = input("Enter stadium name: ")
        opening_date = input("Enter opening date (YYYY-MM-DD): ")
        country = input("Enter country: ")
        city = input("Enter city: ")
        capacity = int(input("Enter capacity: "))
        return cls(name, opening_date, country, city, capacity)


stadium1 = Stadium.create_from_input()
print("\nStadium Information:")
print(stadium1)
