marks = int(input("Enter your Marks: "))

if marks < 0 or marks > 100:
    print("Invalid Marks")
    exit()

if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
else:
    grade = 'F'
    print('Agle Saal Firr se ana')

print("Grade:", grade)