#Find first non repeated character
input_str = input("Enter a string: ")
for i in input_str:
    if input_str.count(i) == 1:
        print("First non-repeated character:", i)
        break