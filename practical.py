class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def display_fraction(self):
        print(f"{self.numerator}/{self.denominator}")

    def add(self, other_fraction):
        result_numerator = self.numerator * other_fraction.denominator + other_fraction.numerator * self.denominator
        result_denominator = self.denominator * other_fraction.denominator
        return Fraction(result_numerator, result_denominator)

    def subtract(self, other_fraction):
        result_numerator = self.numerator * other_fraction.denominator - other_fraction.numerator * self.denominator
        result_denominator = self.denominator * other_fraction.denominator
        return Fraction(result_numerator, result_denominator)

    def multiply(self, other_fraction):
        result_numerator = self.numerator * other_fraction.numerator
        result_denominator = self.denominator * other_fraction.denominator
        return Fraction(result_numerator, result_denominator)

    def divide(self, other_fraction):
        result_numerator = self.numerator * other_fraction.denominator
        result_denominator = self.denominator * other_fraction.numerator
        return Fraction(result_numerator, result_denominator)


fraction1 = Fraction(1, 2)
fraction2 = Fraction(2, 4)

fraction1.display_fraction()
fraction2.display_fraction()

result_addition = fraction1.add(fraction2)
result_addition.display_fraction()

result_addition = fraction1.subtract(fraction2)
result_addition.display_fraction()

result_addition = fraction1.multiply(fraction2)
result_addition.display_fraction()

result_addition = fraction1.divide(fraction2)
result_addition.display_fraction()