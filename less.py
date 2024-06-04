class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def add(self, other):
        common_denominator = self.denominator * other.denominator
        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        return Fraction(new_numerator, common_denominator)

    def subtract(self, other):
        common_denominator = self.denominator * other.denominator
        new_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        return Fraction(new_numerator, common_denominator)

    def multiply(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def divide(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)


fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 4)

print("Дріб 1:", fraction1)
print("Дріб 2:", fraction2)

result_addition = fraction1.add(fraction2)
print("Додавання:", result_addition)

result_subtraction = fraction1.subtract(fraction2)
print("Віднімання:", result_subtraction)

result_multiplication = fraction1.multiply(fraction2)
print("Множення:", result_multiplication)

result_division = fraction1.divide(fraction2)
print("Ділення:", result_division)
