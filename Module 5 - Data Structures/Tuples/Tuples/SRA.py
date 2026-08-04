students = (
    # Data Science (10):
    ("Ali", 85, "Data Science"),
    ("Ahmed", 91, "Data Science"),
    ("Bilal", 78, "Data Science"),
    ("Hamza", 88, "Data Science"),
    ("Usman", 95, "Data Science"),
    ("Ahsan", 72, "Data Science"),
    ("Zain", 81, "Data Science"),
    ("Saad", 90, "Data Science"),
    ("Talha", 67, "Data Science"),
    ("Farhan", 84, "Data Science"),

    # Artificial Intelligence (10):
    ("Sara", 92, "Artificial Intelligence"),
    ("Ayesha", 87, "Artificial Intelligence"),
    ("Hira", 76, "Artificial Intelligence"),
    ("Fatima", 96, "Artificial Intelligence"),
    ("Iqra", 83, "Artificial Intelligence"),
    ("Noor", 71, "Artificial Intelligence"),
    ("Mahnoor", 89, "Artificial Intelligence"),
    ("Laiba", 80, "Artificial Intelligence"),
    ("Anum", 94, "Artificial Intelligence"),
    ("Mariam", 77, "Artificial Intelligence"),

    # Computer Science (10):
    ("Kashif", 86, "Computer Science"),
    ("Salman", 79, "Computer Science"),
    ("Adnan", 93, "Computer Science"),
    ("Danish", 82, "Computer Science"),
    ("Imran", 74, "Computer Science"),
    ("Noman", 91, "Computer Science"),
    ("Shahzaib", 69, "Computer Science"),
    ("Waqar", 88, "Computer Science"),
    ("Asad", 97, "Computer Science"),
    ("Junaid", 84, "Computer Science"),

    # Cyber Security (10):
    ("Abdullah", 90, "Cyber Security"),
    ("Rehan", 73, "Cyber Security"),
    ("Yasir", 85, "Cyber Security"),
    ("Kamran", 92, "Cyber Security"),
    ("Fahad", 78, "Cyber Security"),
    ("Sajid", 81, "Cyber Security"),
    ("Haris", 95, "Cyber Security"),
    ("Rizwan", 87, "Cyber Security"),
    ("Basit", 76, "Cyber Security"),
    ("Owais", 89, "Cyber Security"),

    # Software Engineering (10):
    ("Adeel", 83, "Software Engineering"),
    ("Hasnain", 91, "Software Engineering"),
    ("Shayan", 75, "Software Engineering"),
    ("Huzaifa", 86, "Software Engineering"),
    ("Muzammil", 94, "Software Engineering"),
    ("Taimoor", 79, "Software Engineering"),
    ("Umer", 88, "Software Engineering"),
    ("Zeeshan", 72, "Software Engineering"),
    ("Sameer", 96, "Software Engineering"),
    ("Arham", 84, "Software Engineering")
)
print("=" * 30)
print("  STUDENT RECORDS ANALYZER")
print("=" * 30)

while True :
    print("1. Display All Students")
    print("2. Search Student")
    print("3. Find Topper")
    print("4. Find Lowest Scorer")
    print("5. Calculate Average Marks")
    print("6. Display Students Above Given Marks")
    print("7. Display Students By Department")
    print("8. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1 :
        for name, mark, dep in students :
            print(f"Name: {name}")
            print(f"Marks: {mark}")
            print(f"Department: {dep}")
            print("-" * 10)

    elif choice == 2 :
        search_name = input("Enter The Student Name: ")
        found = False
        for name , mark, dep in students :
            if (search_name == name) :
                 print("-" * 30)
                 print(f"Name: {name}")
                 print(f"Marks: {mark}")
                 print(f"Department: {dep}")
                 found = True
                 print("-" * 30)
                 break
        if found == False :
            print("-" * 25)
            print("Student Not Found.")
            print("-" * 25)

    elif choice == 3 :
        topper = students[0]
        for name, mark, dep in students :
            if mark > topper[1] :
                topper = (name,mark,dep)
        name, mark, dep = topper
        print("_" * 30)
        print(f"Name: {name}")
        print(f"Marks: {mark}")
        print(f"Department: {dep}")
        print("_" * 30)

    elif choice == 4 :
        lowest = students[0]
        for name, mark, dep in students :
            if mark < lowest[1] :
                lowest = (name,mark,dep)
        name, mark, dep = lowest
        print("_" * 30)
        print(f"Name: {name}")
        print(f"Marks: {mark}")
        print(f"Department: {dep}")
        print("_" * 30)

    elif choice == 5 :
        total = 0
        for name, mark, dep in students :
            total += mark
        average = total/len(students)
        print("_" * 30)
        print(f"Average Marks Of All the Programs is: {average:.2f}")
        print("_" * 30)

    elif choice == 6 :
        min_marks = int(input("Enter the minimum Marks:"))
        found = False
        for name, mark, dep in students :
            if mark > min_marks :
                 print(f"Name: {name}")
                 print(f"Marks: {mark}")
                 print(f"Department: {dep}")
                 found = True
                 print("-" * 10)
        if found == False :
                print("No Student Meets the Minimum Marks Requirement.")

    elif choice == 7 :
        ent_dep = input("Enter Department: ")
        found = False
        for name, mark, dep in students :
            if ent_dep == dep :
                 print(f"Name: {name}")
                 print(f"Marks: {mark}")
                 print(f"Department: {dep}")
                 found = True
                 print("-" * 10)
        if found == False :
                print("No Such Department Found.")

    elif choice == 8 :
        print("Thank You For Using SRA. Take Care.")
        break
    else :
        print("OOPS! Invalid Choice!")
