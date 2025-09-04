#Polymorphism in Function
def add(a,b):
    return (a+b, a*b, a/b, a**b)
    

x= int(input("Enter the number : "))
y= int(input("Enter the number : "))
sum = add(x,y)
print(sum)