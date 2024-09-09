#!/usr/bin/env python3

#!/usr/bin/env python3

def greet_programmer():
    # Outputs "Hello, programmer!" to the terminal
    print("Hello, programmer!")

def greet(name):
    # Outputs "Hello, name!" where "name" is the passed argument
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    # Outputs "Hello, name!" or "Hello, programmer!" if no name is provided
    print(f"Hello, {name}!")

def add(num1, num2):
    # Returns the sum of num1 and num2
    return num1 + num2

def halve(number):
    # Returns the number divided by two
    return number / 2
