# prime number
n = int(input("Enter a number: "))

is_prime = True 

if n>1:
    for i in range(2,n):
        if (n%i)==0:
            is_prime= False
            break
print("Prime") if is_prime else print("Not Prime")