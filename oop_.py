#1
class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount < 0:
            print("Error: Cannot deposit a negative amount")
            return
        self._balance += amount

    def withdraw(self, amount):
        if amount < 0:
            print("Error: Cannot withdraw a negative amount")
            return
        if self._balance < amount:
            print("Error: Insufficient funds")
            return
        self._balance -= amount


account = BankAccount(100)

account.withdraw(50)
print("Balance after withdrawal:", account.balance)

account.withdraw(70)

account.deposit(200)

account.withdraw(300)

print("Final balance:", account.balance)
#2
class TemperatureSensor:
    def __init__(self):
        self._temperature = 0

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if not -40 <= value <= 80:
            raise ValueError("Temperature out of range (-40 to 80 degrees Celsius)")
        self._temperature = value


sensor = TemperatureSensor()

sensor.temperature = 25
print("Current temperature:", sensor.temperature)

sensor.temperature = 100
print("Current temperature:", sensor.temperature)


#3
class TextModifier:
    def __init__(self, text):
        self.text = text

    def to_uppercase(self):
        self.text = self.text.upper()

    def to_lowercase(self):
        self.text = self.text.lower()

    def remove_spaces(self):
        self.text = ''.join(self.text.split())

    def encrypt(self, shift):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        shifted_alphabet = alphabet[shift:] + alphabet[:shift]
        table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
        self.text = self.text.translate(table)


modifier = TextModifier("Hello World!")

modifier.to_uppercase()
print("Text in uppercase:", modifier.text)

modifier.to_lowercase()
print("Text in lowercase:", modifier.text)

modifier.remove_spaces()
print("Text with spaces removed:", modifier.text)

modifier = TextModifier("Hello World!")
modifier.encrypt(3)
print("Encrypted text:", modifier.text)
