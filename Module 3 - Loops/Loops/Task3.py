print(f"The numbers from 1 to 10 are:")

for i in range(1,11):
    print(i)

print(f"Even numbers from 2 to 20 are:")

for i in range(2,22,2):
    print(i)

num = int(input("Enter the number: "))
print("The Table is : ")
i = 1
while i <= 10:
    print(f"{num} * {i} = {num*i}")
    i = i+1    


a = 5
while a >= 1:
    print(a)
    a = a-1
print("Blast Off")


b = 1

while b != 0 :
    b = int(input(f"Enter a number (0 to stop):"))
    print(b)
print(f"Program Stopped.")

for i in range(1,10):
    if i == 6:
        break
    print(i)

for i in range(1,10):
    if i == 5 :
        continue
    print(i)



