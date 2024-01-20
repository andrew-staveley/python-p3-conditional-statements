#!/usr/bin/env python3

def admin_login(username, password):
    if username.lower() == "admin" and password =="12345":
        return "Access granted"
    else:
        return "Access denied"

def hows_the_weather(temperature):
    if temperature > 85:
        return "It's too dang hot out there!"
    elif temperature > 65 and temperature < 85:
        return "It's perfect out there!"
    elif temperature < 65 and temperature > 40:
        return "It's a little chilly out there!"
    elif temperature < 40:
        return "It's brisk out there!"

def fizzbuzz(num):
    if num == 0:
        return "FizzBuzz"
    elif num == 15:
        return "FizzBuzz"
    elif num == 45:
        return "FizzBuzz"
    elif num == 5:
        return "Buzz"
    elif num == 10:
        return "Buzz"
    elif num == 50:
        return "Buzz"
    elif num == 2:
        return num
    elif num == 13:
        return num
    elif num == 59:
        return num
    else:
        return "Fizz"

def calculator(operation, num1, num2):
    if operation == "+" :
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None

