#1. Creating Dictionary:
student = {
"name" : "Abdullah",
"age" : 20,
"program" : "Data Science",
"university" : "University of Peshawar"
}
print(student)
print(type(student))

empty_dict = {}
print(empty_dict)
print(type(empty_dict))

#2. Accessing values:
student = {
"name" : "Abdullah",
"age" : 20,
"program" : "Data Science",
"university" : "University of Peshawar"
}
print(f'Name:{student["name"]}')
print(f'Program:{student["program"]}')
print(f'University:{student["university"]}')

print(student.get("City", "Not Available"))
print(student.get("age"))

#3. Updating Dictionary:
student = {
    "name": "Abdullah",
    "age": 20,
    "program": "Data Science"
}
student["city"] = "Chitral"
student["age"] = 21
student.update({"program": "Software Engineering",
                "university": "University of Peshawar"})
print(student)

student = {
    "name": "Abdullah",
    "program": "Data Science"
}
student["program"] = "Machine Learning"
student["age"] = 20
student.update({"city": "Chitral",
                "university": "UOP"})
print(student)

#4. Dictionay Methods:

student = {
    "name": "Abdullah",
    "age": 20,
    "program": "Data Science",
    "university": "University of Peshawar"
}
print(student.keys())
print(student.values())
print(student.items())
removed = student.pop("name")
print(removed)
print(student)

data = {
    "username": "abdullah12",
    "passward": 2444666666,
    "social_app": "Facebook"
}
rem = data.popitem()
print(rem)
print(data)
data.clear()
print(data)


data = {
    "username": "abdullah12",
    "passward": 2444666666,
    "social_app": "Facebook"
}
copy_data = data.copy()
copy_data["location"] = "Chitral"
print(copy_data)

record = {
    "name": "Abdullah",
    "Roll No": 5,
    "program": "Data Science"
}
result = record.setdefault("program", "Machine Learning")
result1 = record.setdefault("country", "Pakistan")
print(result)
print(result1)
print(record)


