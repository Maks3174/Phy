#1
class Person:
    def __init__(self, name, age, phone_number, city, country, address):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.city = city
        self.country = country
        self.address = address

    def __str__(self):
        return f"Ім'я: {self.name}, Вік: {self.age}, Телефон: {self.phone_number}, Місто: {self.city}, Країна: {self.country}, Адреса: {self.address}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age and self.phone_number == other.phone_number and self.city == other.city and self.country == other.country and self.address == other.address

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age

    def __ne__(self, other):
        return self.age != other.age

person1 = Person("Іван", 25, "+123456789", "Київ", "Україна", "вул. Шевченка, 1")
person2 = Person("Петро", 30, "+987654321", "Львів", "Україна", "пл. Ринок, 5")

print(person1 < person2)
print(person1 <= person2)
print(person1 == person2)
print(person1 != person2)
print(person1 > person2)  #
print(person1 >= person2)

print(person1)
print(person2)

#2
class City:
    def __init__(self, name, region, country, population, postal_code, phone_code):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.postal_code = postal_code
        self.phone_code = phone_code

    def __str__(self):
        return f"Назва міста: {self.name}, Регіон: {self.region}, Країна: {self.country}, Населення: {self.population}, Поштовий індекс: {self.postal_code}, Телефонний код: {self.phone_code}"

    def __eq__(self, other):
        return self.name == other.name and self.region == other.region and self.country == other.country and self.population == other.population and self.postal_code == other.postal_code and self.phone_code == other.phone_code

    def __lt__(self, other):
        return self.population < other.population

    def __le__(self, other):
        return self.population <= other.population

    def __gt__(self, other):
        return self.population > other.population

    def __ge__(self, other):
        return self.population >= other.population

    def __ne__(self, other):
        return self.population != other.population

city1 = City("Київ", "Київська область", "Україна", 2800000, 10000, "+380")
city2 = City("Львів", "Львівська область", "Україна", 720000, 79000, "+380")

print(city1 < city2)
print(city1 <= city2)
print(city1 == city2)
print(city1 != city2)
print(city1 > city2)
print(city1 >= city2)

print(city1)
print(city2)


#3
class Country:
    def __init__(self, name, continent, population, phone_code, capital, cities):
        self.name = name
        self.continent = continent
        self.population = population
        self.phone_code = phone_code
        self.capital = capital
        self.cities = cities

    def __str__(self):
        return f"Назва країни: {self.name}, Континент: {self.continent}, Населення: {self.population}, Телефонний код: {self.phone_code}, Столиця: {self.capital}, Міста: {', '.join(self.cities)}"

    def __eq__(self, other):
        return self.name == other.name and self.continent == other.continent and self.population == other.population and self.phone_code == other.phone_code and self.capital == other.capital and self.cities == other.cities

    def __lt__(self, other):
        return self.population < other.population

    def __le__(self, other):
        return self.population <= other.population

    def __gt__(self, other):
        return self.population > other.population

    def __ge__(self, other):
        return self.population >= other.population

    def __ne__(self, other):
        return self.population != other.population

country1 = Country("Україна", "Європа", 40000000, "+380", "Київ", ["Київ", "Львів", "Одеса"])
country2 = Country("Німеччина", "Європа", 83000000, "+49", "Берлін", ["Берлін", "Мюнхен", "Гамбург"])

print(country1 < country2)
print(country1 <= country2)
print(country1 == country2)
print(country1 != country2)
print(country1 > country2)
print(country1 >= country2)

print(country1)
print(country2)

#4
class Watch:
    def __init__(self, model_name, manufacturer, year, price, type_of_watch):
        self.model_name = model_name
        self.manufacturer = manufacturer
        self.year = year
        self.price = price
        self.type_of_watch = type_of_watch

    def __str__(self):
        return f"Модель: {self.model_name}, Виробник: {self.manufacturer}, Рік випуску: {self.year}, Ціна: {self.price}, Тип: {self.type_of_watch}"

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price

    def __gt__(self, other):
        return self.price > other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __ne__(self, other):
        return self.price != other.price

watch1 = Watch("G-Shock", "Casio", 2020, 150, "наручний")
watch2 = Watch("Oyster Perpetual", "Rolex", 2018, 5000, "наручний")

print(watch1 < watch2)
print(watch1 <= watch2)
print(watch1 == watch2)
print(watch1 != watch2)
print(watch1 > watch2)
print(watch1 >= watch2)

print(watch1)
print(watch2)


#5
class Website:
    def __init__(self, name, address, description):
        self.name = name
        self.address = address
        self.description = description

    def __str__(self):
        return f"Назва: {self.name}, Адреса: {self.address}, Опис: {self.description}"

    def __eq__(self, other):
        return self.name == other.name and self.address == other.address and self.description == other.description

    def __lt__(self, other):
        return self.name < other.name

    def __le__(self, other):
        return self.name <= other.name

    def __gt__(self, other):
        return self.name > other.name

    def __ge__(self, other):
        return self.name >= other.name

    def __ne__(self, other):
        return self.name != other.name

website1 = Website("Google", "https://www.google.com", "Пошукова система та інтернет-компанія")
website2 = Website("Facebook", "https://www.facebook.com", "Соціальна мережа")


print(website1 < website2)
print(website1 <= website2)
print(website1 == website2)
print(website1 != website2)
print(website1 > website2)
print(website1 >= website2)


print(website1)
print(website2)
