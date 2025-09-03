age = input("Enter your age: ")
if age.isdigit():
    age = int(age)
    if age < 18:
        print("You are a minor.")
    else:
        print("You are an adult.")
else:
    print("Invalid input. Please enter a valid age.")    