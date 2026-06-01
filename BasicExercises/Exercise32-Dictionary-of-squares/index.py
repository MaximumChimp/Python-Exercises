#PROBLEM:Create a dictionary where the keys are numbers from 1 to 10 and the values are the squares of those numbers (e.g., 2: 4, 3: 9).
#PURPOSE:This exercise explores “Data Mapping.” It demonstrates how dictionaries can be used to store pre-calculated mathematical relationships, essentially acting as a “lookup table” that can replace expensive repetitive calculations.
res = {}

def squared_dict(n):
    squared = 0
    for i in range(1,n+1):
        squared = i * i
        res[i] = squared
    return res
print(squared_dict(10))
