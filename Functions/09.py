#Funcion with "Kwargs"
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Python",power="Easy to learn")
print_kwargs(power="Easy to learn",name="Python")
print_kwargs(name="Python",power="Easy to learn",enemy="Java",friend="C++")