import math
import os
import colorama
from colorama import Fore
print(Fore.CYAN+"""
           __                     _     
    ____  / /_  ____  ___  ____  (_)  __
   / __ \/ __ \/ __ \/ _ \/ __ \/ / |/_/
  / /_/ / / / / /_/ /  __/ / / / />  <  
 / .___/_/ /_/\____/\___/_/ /_/_/_/|_|  
/_/               V 1.0.0
____________________________
|<01> Sum                  |
|<02> Subtraction          |
|<03> Multiplication       |
|<04> Division             |
|<05> Sine                 |
|<06> Cosine               |
|<07> Tangent              |
|<08> Quadratic equation1  |
|<09> Quadratic equation2  |
|<10> History              |
|__________________________|
|<98> Credits              |
|<99> Social Media         |
|<00> Back                 |
|__________________________|"""+Fore.WHITE)

while True:
    ope = input("Enter the desired operation number: ")
    if ope == "00":
        break
    elif ope == "10":
        with open("zzz.txt", "r") as file:
            print(file.read())
    elif ope == "01":
        num_variables = int(input("Enter the number of variables for summation: "))
        variables = [float(input(f"Enter the value of variable {chr(97 + i)}: ")) for i in range(num_variables)]
        result = sum(variables)
        print("The result of the summation is:", result)
        with open("zzz.txt", "a") as file:
            file.write(f"Summation of {variables} = {result}\n")
    elif ope == "02":
        a = float(input("Enter the first number for subtraction: "))
        b = float(input("Enter the second number for subtraction: "))
        result = a - b
        print("The result of the subtraction is:", result)
        with open("zzz.txt", "a") as file:
            file.write(f"Subtraction of {a} and {b} = {result}\n")
    elif ope == "03":
        num_variables = int(input("Enter the number of variables for multiplication: "))
        variables = [float(input(f"Enter the value of variable {chr(97 + i)}: ")) for i in range(num_variables)]
        result = 1
        for variable in variables:
            result *= variable
        print("The result of the multiplication is:", result)
        with open("zzz.txt", "a") as file:
            file.write(f"Multiplication of {variables} = {result}\n")
    elif ope == "04":
        a = float(input("Enter the numerator for division: "))
        b = float(input("Enter the denominator for division: "))
        if b == 0:
            print("Error: division by zero")
            with open("zzz.txt", "a") as file:
                file.write(f"Division of {a} and {b} = Error: division by zero\n")
        else:
            result = a / b
            print("The result of the division is:", result)
            with open("zzz.txt", "a") as file:
                file.write(f"Division of {a} and {b} = {result}\n")
    elif ope == "05":
        angle = float(input("Enter the angle in degrees to calculate the sine: "))
        result = math.sin(math.radians(angle))
        print("The result of the sine is:", result)
        with open("zzz.txt", "a") as file:
            file.write(f"Sine of {angle} = {result}\n")
    elif ope == "06":
        angle = float(input("Enter the angle in degrees to calculate the cosine: "))
        result = math.cos(math.radians(angle))
        print("The result of the cosine is:", result)
        with open("zzz.txt", "a") as file:
            file.write(f"Cosine of {angle} = {result}\n")
    elif ope == "07":
        angle = float(input("Enter the angle in degrees to calculate the tangent: "))
        result = math.tan(math.radians(angle))
        print("The result of the tangent is:", result)
        with open("zzz.txt", "a") as file:
            file.write(f"Tangent of {angle} = {result}\n")
    elif ope == "08":
        a = float(input("Enter the coefficient a of the first degree equation: "))
        b = float(input("Enter the coefficient b of the first degree equation: "))
        if a == 0:
            print("The equation is not of the first degree")
            with open("zzz.txt", "a") as file:
                file.write(f"First degree equation with a={a} and b={b} = The equation is not of the first degree\n")
        else:
            result = -b/a
            print(f"The result of the first degree equation is: {result}")
            with open("zzz.txt", "a") as file:
                file.write(f"First degree equation with a={a} and b={b} = {result}\n")
    elif ope == "09":
        a = float(input("Enter the coefficient a of the second degree equation: "))
        b = float(input("Enter the coefficient b of the second degree equation: "))
        c = float(input("Enter the coefficient c of the second degree equation: "))
        delta = b**2 - 4*a*c
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            print(f"The roots of the second degree equation are: {x1} and {x2}")
            with open("zzz.txt", "a") as file:
                file.write(f"Second degree equation with a={a}, b={b}, and c={c} gives roots x1 and x2\n")
    elif ope == "98":
        print("Developed by Phoenix and Stakzxy.")
    elif ope == "99":
        print(Fore.CYAN+"Github: stakzxy\nDiscord: .xineohp"+Fore.WHITE)
    else:
        print("Invalid option")
