#Factorial using while loop
n = int(input("Enter a number: "))
factorial = 1
while n > 0:
    factorial *= n
    n -= 1
print("Factorial:", factorial)

# using for loop

n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("Factorial:", factorial)
