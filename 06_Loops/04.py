#reverse a string using loop
input_str = input("Enter a string: ")
reversed_str = ""
for char in input_str:
    reversed_str = char + reversed_str
print("Reversed string:", reversed_str)
