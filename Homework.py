class Person:
    def __init__(self, full_name, date_of_birth, phone_number, city, country, home_address):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        self.city = city
        self.country = country
        self.home_address = home_address

    def __str__(self):
        return f"Full Name: {self.full_name}\nDate of Birth: {self.date_of_birth}\nPhone Number: {self.phone_number}\nCity: {self.city}\nCountry: {self.country}\nHome Address: {self.home_address}"

    def update_phone_number(self, new_phone_number):
        self.phone_number = new_phone_number
        print("Phone number updated.")


person1 = Person("John Doe", "01-01-1990", "+123456789", "New York", "USA", "123 Main St")
print("Person Information:")
print(person1)

person1.update_phone_number("+987654321")
print("\nUpdated Person Information:")
print(person1)
