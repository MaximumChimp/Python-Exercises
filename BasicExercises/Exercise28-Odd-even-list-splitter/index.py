#PROBLEM : Start with a list of 10 numbers. Iterate through them and sort them into two separate lists: one for even numbers and one for odd numbers.

numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]

even_list = [even for even in numbers if even % 2 ==0]
odd_list = [odd for odd in numbers if odd % 2 != 0]

print(f"Even numbers: {even_list}")
print(f"Odd numbers: {odd_list}")