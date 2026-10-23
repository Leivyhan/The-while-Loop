integer = int(input("Enter n (positive integer): "))

n = integer
while n <= 0:
    print("Your input is not a positive integer, try again.")
    integer = int(input("Integer (positive): "))
    n = integer

while n > 0:
    print(n, end=" ")
    n -= 1

print("Liftoff!")