#Sloving problems:
#1. Remove the duplicates from a list using set:

numbers = [10, 20, 10, 30, 20, 40, 30, 50]
unique_elements = set()
for i in numbers :
    unique_elements.add(i)
print(unique_elements)

#2. Find Common elements in sets:
A = {10, 20, 30, 40, 50}
B = {30, 40, 50, 60, 70}
common = A & B # A.intersection(B)
print(f"Common Elemnts are:{common}")

#3. Find Missing Class:
required_classes = {"Apple", "Banana", "Orange", "Potato"}
available_classes = {"Apple", "Orange", "Potato"}
missing_class = required_classes.difference(available_classes)
print(f"Missing Class is :{missing_class}")

#4. Find the unique elements from the sets:
A = {"Python", "C++", "Java"}
B = {"Python", "JavaScript", "C++"}
unique = A ^ B
print(f"Elements that are unique in both sets are:{unique}")

#5. Write a code that checks available formats in a set:
allowed_formats = {"jpg", "jpeg", "png", "webp"}
user_input = input("Enter the file extension:")
if user_input in allowed_formats :
    print("Format allowed.")
else :
    print("Format not allowed.")

#6.find the numbers that occur more than once:
data = [10, 20, 30, 20, 40, 50, 10, 30]
seen = set()
duplicates = set()
for number in data :
    if number in seen :
        duplicates.add(number)
    seen.add(number)
print(duplicates)
    
