#Default Parameter Value

def greet(name= "User"):
    return "Hello, "+ name + "!"

x= input("Enter Your Name: ")
Name=greet(x)
print(Name)