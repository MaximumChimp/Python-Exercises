#PROBLEM: Take two lists and find the elements that appear in both. Use Sets to perform the operation.
#PURPOSE: This exercise explores “Mathematical Set Operations.” Finding intersections is vital for recommendation engines (e.g., finding “mutual friends” or “shared interests”). It demonstrates why using the right data structure (Set) is more efficient than nested loops.

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

set_a = set(list_a)
set_b = set(list_b)

common = set_a & set_b


print(f'Common Elements: {common}')