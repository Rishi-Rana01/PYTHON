# validate input 
while True:
    num=int(input("Enter value b/w 1 and 10 : "))

    if 1 <= num <= 10:
        print("Valid input:", num)
        break
    else:
        print("Invalid input. Please try again.")