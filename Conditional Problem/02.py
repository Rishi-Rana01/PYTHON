age = input("Enter your age : ")
age = int(age)
day = "Wednesday"

price = 12 if age >=18 else 8

if day == "Wednesday":
    price = price-2

print("Ticket Price is for you is $",price)