#PROBLEM : Iterate through a given list of numbers and print only those numbers which are divisible by 5.
#PURPOSE : This exercise teaches the use of the modulo operator (%) and loop filtering. In data processing, you often need to sift through large datasets to extract subsets that meet mathematical criteria.

num_list = [10, 20, 33, 46, 55]

for num in num_list:
    if num % 5 ==0:
        print(f'Divisible by 5: {num}')

#List Comprehension created new list
new_list = [num for num in num_list if num % 5 == 0]
print(f'Divisible by 5: {new_list}')