# Python Calculator

import math

operator = input("Enter an Operator (+, -, *, /): ")
num1 = float(input("Enter Number 1: "))
num2 = float(input("Enter Number 2: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else: 
    print(f"{operator} is invalid operator. ")

print(round(result, 3))