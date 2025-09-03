# Countig Positive no
numbers = [1,-2,3,-4,5,-6,-7,-8,9,10]
positive_num_count = 0
Total =0

for num in numbers:
    if num>0:
        positive_num_count += 1
        Total = Total+num
print(positive_num_count)
print(Total)
