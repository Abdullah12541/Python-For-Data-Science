#Addition of Two Numbers
def add(num1, num2):
    return num1 + num2

result = add(10, 20)

print(f"The sum is {result}.")

#Maximum of Two Numbers
def maximum(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

result1 = maximum(40, 20)
print(f"The Largest number is {result1}.")

#Even_Odd Checker
number = int(input("Enter the number:"))
def even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
result2 = even_odd(number)
print(f"The given number is {result2}.")

#Celsius To Fahrenheit Conveter 
celsius = int(input("Enter the Temperature in °C:"))
def converter(celsius):
    return  (celsius * 9/5) + 32
    
result3 = converter(celsius)
print(f"The Temperature in Fahrenheit is {result3}")


#Area of Rectangle
Length = int(input("Enter the Length: "))
Width = int(input("Enter the Width: "))

def Area(Length,Width):
    return Length*Width
result4 = Area(Length,Width)
print(f"The Area of Rectangle is {result4}.")

#Multiplication Table of any Number
n = int(input("Enter the number: "))

def table(n):
    for i in range(1, 11):
        print(f"{n} * {i} = {n*i}")

table(n)

#Factorial of any number
n = int(input("Enter a number: "))

def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact

result = factorial(n)

print(result)
        


