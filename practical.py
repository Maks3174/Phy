class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def __str__(self):
        return f"Стадіон: {self.name}, Дата відкриття: {self.opening_date}, Країна: {self.country}, Місто: {self.city}, Місткість: {self.capacity}"

    def __eq__(self, other):
        return self.capacity == other.capacity

    def __lt__(self, other):
        return self.capacity < other.capacity

    def __le__(self, other):
        return self.capacity <= other.capacity

    def __gt__(self, other):
        return self.capacity > other.capacity

    def __ge__(self, other):
        return self.capacity >= other.capacity

stadium1 = Stadium("Camp Nou", "1957-09-24", "Spain", "Barcelona", 99354)
stadium2 = Stadium("Wembley Stadium", "2007-03-17", "England", "London", 90000)

print(stadium1 < stadium2)
print(stadium1 == stadium2)

print(stadium1)
print(stadium2)

