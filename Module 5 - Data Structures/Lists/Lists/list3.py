# #Membership Operators (in, not in): Checks whether an element
# exists in a list or not.

subjects = ["English", "Math", "Science", "Computer Science"]

fruits = ["Apple", "Banana", "Orange", "Mango", "Grapes"]

predictions = ["Cat", "Dog", "Birds", "Horse"]

print("Math" in subjects)
print("Urdu" in subjects)
print("Orange" in fruits)
print("Potato" in fruits)
print("Horse" in predictions)

print("Science" not in subjects)
print("Physics" not in subjects)
print("Apple" not in fruits)
print("Banana" not in predictions)
print("Cat" not in predictions)

math_exists = "Math" in subjects
print(math_exists)

is_cat = "Cat" not in predictions
print(is_cat)

if "Science" in subjects:
    print("Science subject is available.")
else:
    print("Science subject is not available.")

if "Potato" in fruits:
    print("Potato is in list.")
else:
    print("Potato is not in list.")

if "Dog" in predictions:
    print("Dog is in predictions.")
else:
    print("Dog is not in predictions.")

if "Cat" not in predictions:
    print("Cat is not in predictions.")
else:
    print("Cat is in predictions.")