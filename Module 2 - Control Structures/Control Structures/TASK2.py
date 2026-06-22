name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))
attendance = int(input("Enter your attendance %: "))

if age >= 18 :
    print(f"You are eligible to vote.")
else:
    print(f"You are not eligible to vote.")

if marks >= 90 :
    print(f"Your garde is A.")
elif marks >= 80:
    print(f"Your grade is B.")
elif marks >= 70 :
    print(f"Your grade is C.")
elif marks >= 60 :
    print(f"Your grade is D.")
elif marks >= 50 :
    print(f"Your grade is E.")
else:
    print(f"You are failed.")

if marks >= 50 and attendance >= 75 :
    print(f"You are passed.")
else:
    print(f"You are failed.")

if marks >= 90 or attendance >= 95 :
    print(f"Scholarship Granted.")
else:
    print(f"Scholarship not Granted.")

student = True
if not student :
    print(f"I am not a student.")
else:
    print(f"I am a student.")