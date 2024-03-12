class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Внесено {amount} грошей. Новий баланс: {self.balance}")
        else:
            print("Недійсна сума для внесення.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Знято {amount} грошей. Новий баланс: {self.balance}")
            else:
                print("Недостатньо коштів на рахунку.")
        else:
            print("Недійсна сума для зняття.")


account1 = BankAccount("Іван Петрович")
account1.deposit(100)
account1.withdraw(50)
account1.withdraw(80)
account1.deposit(-20)
