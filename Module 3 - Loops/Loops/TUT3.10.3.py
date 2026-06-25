num = int(input("Enter a number:"))

for i in range(1, num+1):
    if i % 2 == 0:
        continue

    if i == 11:
        break

    print(i)