#7. Built in Functions:
student_marks = {
    "Ali": 85,
    "Ahmad": 72,
    "Abdullah": 91,
    "Sara": 88,
    "Zain": 0
}
result1 = len(student_marks.keys())
result2 = max(student_marks.values())
result3 = max(student_marks.keys())
result4 = min(student_marks.values())
result5 = min(student_marks.keys())
result6 = sum(student_marks.values())
result7 = sorted(student_marks.keys())
result8 = sorted(student_marks.values())
result9 = any(student_marks.values())
result10 = all(student_marks.values())

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)
print(result9)
print(result10)
print(type(student_marks))
print(type(student_marks.keys()))
print(type(student_marks.values()))

#8. Traversing Dictionaries:
student = {
    "name": "Abdullah",
    "age": 20,
    "program": "Data Science",
    "university": "University of Peshawar"
}
for key in student :
    print(key)
for value in student.values() :
    print(value)
for key, value in student.items() :
    print(f"{key}: {value}" )

student_marks = {
    "Ali": 85,
    "Ahmad": 72,
    "Abdullah": 91,
    "Sara": 88,
    "Zain": 0
}

for key, value in student_marks.items() :
    if value >= 80 :
        print(f"{key}: {value}")

student_marks = {
    "Ali": 85,
    "Ahmad": 72,
    "Abdullah": 91,
    "Sara": 88,
    "Zain": 0
}
total = 0
count = 0
for value in student_marks.values() :
    total += value
    count += 1
average = total/count
print(average)

student_marks = {
    "Ali": 85,
    "Ahmad": 72,
    "Abdullah": 91,
    "Sara": 88,
    "Zain": 0
}
highest_student = None
highest_marks = 0
for key, value in student_marks.items() :
    if value > highest_marks :
        highest_marks = value
        highest_student = key
print(highest_student, highest_marks)

student_marks = {
    "Ali": 85,
    "Ahmad": 72,
    "Abdullah": 91,
    "Sara": 88,
    "Zain": 0
}
total = 0
count = 0
for value in student_marks.values() :
    total += value
    count += 1
average = total/count
for key, value in student_marks.items() :
    if value > average :
        print(key, value)

above_average = 0
for key, value in student_marks.items() :
    if value > average :
        above_average += 1
print(above_average)

