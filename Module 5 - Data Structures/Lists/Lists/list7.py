#Nested List:

students = [
    ["Ali", 85],
    ["Ahmed", 92],
    ["Sara", 88]
]

students[0][1] = 95
students[1][0] = "Bilal"
print(students[0])
print(students[2][1])
print(students)

students1 = [
    ["Ali", 85],
    ["Ahmed", 92],
    ["Sara", 88]
]

students1.append(["Bilal", 90])
students1.insert(1, ["Fatima", 95])
students1.remove(["Sara", 88])
students1.pop()
del students1[0]
print(students1)

#List Comprehension:

numbers = [5, 12, 7, 20, 3, 15]

squares = [i**2 for i in numbers]
result = [i for i in numbers if i > 10]
odd_even = ["Even" if i % 2 == 0 else "Odd" for i in numbers]
print(squares)
print(result)
print(odd_even)

#List Traversal:

numbers = [12, 25, 8, 40, 17, 30]

for number in numbers:
    print(number)
    print(number**2)
    if number % 2 == 0 :
        print(number)
    if number % 2 != 0 :
        print(number)

index = 0
while index < len(numbers):
    print(numbers[index])
    print(numbers[index] * 2)
    if numbers[index] > 20 :
        print(numbers[index])
    index +=1

for index ,  value in enumerate(numbers) :
    print(index, value)

for index , value in enumerate(numbers) :
    print(f"Number {index +1} : {value}")

for index , value in enumerate(numbers):
    if index % 2 == 0 :
        print(value)

#Traversing nested lists:

students = [
    ["Ali", 85],
    ["Ahmed", 92],
    ["Sara", 78],
    ["Bilal", 95],
    ["Fatima", 88]
]

for student in students:
    print(student)
for name , mark in students:
    print(name)
for name , mark in students:
    print(mark)
for name , mark in students:
    print(name, mark)

index = 0
while index < len(students) :
    print(students[index])
    index += 1
index = 0
while index < len(students) :
    print(students[index][0], students[index][1])
    index += 1

for index , student in enumerate(students) :
    print(index, student)

for index , student in enumerate(students) :
    print(f"Student {index +1}: {student[0]} {student[1]}")

for index , (name,marks) in enumerate(students) :
    if index % 2 == 0 :
        print(name)