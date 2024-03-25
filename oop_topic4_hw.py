#1
class Fraction:
    number_of_instances = 0

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        Fraction.number_of_instances += 1

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    @staticmethod
    def count_instances():
        return Fraction.number_of_instances


fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 4)
fraction3 = Fraction(5, 6)

print("Number of instances of the Fraction class:", Fraction.count_instances())

#2
class TemperatureConverter:
    temperature_count = 0

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        TemperatureConverter.temperature_count += 1
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        TemperatureConverter.temperature_count += 1
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def get_temperature_count():
        return TemperatureConverter.temperature_count


celsius_temp = 20
fahrenheit_temp = 68

converted_fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius_temp)
converted_celsius = TemperatureConverter.fahrenheit_to_celsius(fahrenheit_temp)

print(f"{celsius_temp} градусів Цельсія дорівнює {converted_fahrenheit} градусам Фаренгейта.")
print(f"{fahrenheit_temp} градусів Фаренгейта дорівнює {converted_celsius} градусам Цельсія.")

print("Кількість підрахунків температури:", TemperatureConverter.get_temperature_count())

#3
class UnitConverter:
    length_count = 0

    @staticmethod
    def meters_to_feet(meters):
        UnitConverter.length_count += 1
        return meters * 3.281

    @staticmethod
    def feet_to_meters(feet):
        UnitConverter.length_count += 1
        return feet / 3.281

    @staticmethod
    def get_length_count():
        return UnitConverter.length_count


meters_length = 10
feet_length = 32.8084

converted_feet = UnitConverter.meters_to_feet(meters_length)
converted_meters = UnitConverter.feet_to_meters(feet_length)

print(f"{meters_length} метрів дорівнює {converted_feet:.2f} футам.")
print(f"{feet_length:.2f} футів дорівнює {converted_meters:.2f} метрам.")

print("Кількість підрахунків довжини:", UnitConverter.get_length_count())


#4
class InformationSystem:
    data = {}

    @classmethod
    def add_user(cls, user_name, contacts):
        cls.data[user_name] = contacts

    @classmethod
    def add_contact(cls, user_name, contact):
        if user_name in cls.data:
            cls.data[user_name].append(contact)
        else:
            cls.data[user_name] = [contact]

InformationSystem.add_user("Bob", ["123456789", "bob@example.com"])
InformationSystem.add_contact("Bob", "bob@gmail.com")

print(InformationSystem.data)
