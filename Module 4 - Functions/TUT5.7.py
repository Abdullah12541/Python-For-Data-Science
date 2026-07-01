#lOCAL VARIABLE Understanding

#1
def city():
    city_name = "Peshawar"
    print(city_name)

city()

#2
def city():
    city_name = "Peshawar"
    city()

    print(city_name)

#3
def age():
    student_age = 20
    print(student_age)

age()
print("Program Finished")

#4
def student():
    name = "Ali"
    print(name)

def teacher():
    print(name)

student()
teacher()