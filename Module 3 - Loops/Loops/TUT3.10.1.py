num = int(input("Enter a number:"))
count = 0

for i in range(1, num+1):
    if i % 2 == 0:
        continue

    count += 1
    print(i)

print(f"Total Odd Numbers printed: {count}")