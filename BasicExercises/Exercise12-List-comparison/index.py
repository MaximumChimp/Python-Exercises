#PROBLEM : Write a function to return True if the first and last number of a given list is the same. If the numbers are different, return False.
#PURPOSE : This exercise introduces “Collection Indexing” and “Boolean Flags.” Comparing data structure boundaries is common in pattern matching and data integrity checks.

def list_comparison(item):
    if item[0] == item[-1]:
        return True
    else:
        return False

result = list_comparison([10,20,30,40,10])
print(result)

result = list_comparison([75, 65, 35, 75, 30])
print(result)
