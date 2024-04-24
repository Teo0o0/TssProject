class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


if 1 == 1:
    print("1")


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof! Woof!")

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            print("Error: Division by zero!")

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        print(f"The {self.make} {self.model} is starting.")

    def stop(self):
        print(f"The {self.make} {self.model} is stopping.")

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Current balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance}")
        else:
            print("Insufficient funds!")

if __name__ == "__main__":
    person = Person("Alice", 30)
    person.greet()

    dog = Dog("Buddy", "Labrador")
    dog.bark()

    calculator = Calculator()
    print("2 + 3 =", calculator.add(2, 3))
    print("5 - 2 =", calculator.subtract(5, 2))
    print("4 * 6 =", calculator.multiply(4, 6))
    print("10 / 2 =", calculator.divide(10, 2))

    car = Car("Toyota", "Camry")
    car.start()
    car.stop()

    account = BankAccount("123456", 1000)
    account.deposit(500)
    account.withdraw(200)
