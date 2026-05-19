number = int(input("Enter a number "))

for count in range(1, 13):
    table = number * count
    print(number, "x", count, "=", table)
