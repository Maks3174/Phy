class Animals:
    def braeth(self):
        print("дихає")
    def move(self):
        print("рухається")
    def eat_food(self):
        print("Їсть")


class Dogs(Animals):
    pass

class Cat(Animals):
    pass

my_dog = Dogs()
my_dog.braeth()