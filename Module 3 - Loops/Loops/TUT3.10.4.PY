num = int(input("Enter a number:"))

for i in range(1, num+1):
    if i % 3 == 0:
        continue
    print(i)