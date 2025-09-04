#Gernator Function with "Yield"
# def count_up_to(max):
#     count = 1
#     while count <= max:
#         yield count
#         count += 1
# for number in count_up_to(5):
#     print(number)  



def even_generator(limit):
    for num in range(limit+1):
        if num % 2 == 0:
            yield num
for even in even_generator(10):
    print(even)