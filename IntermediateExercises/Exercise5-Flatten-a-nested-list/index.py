#PROBLEM: Write a recursive function that takes a list containing other lists (of any depth) and returns a single “flat” list of all elements.
#PURPOSE: Intermediate Python often involves dealing with nested data (like JSON). This exercise teaches Recursion—the ability of a function to call itself—to drill down into nested structures until it finds base values.

def recursive_list(lst):

    flatten_list = []

    for item in lst:
        if isinstance(item, list):
            flatten_list.extend(recursive_list(item))
        else:
            flatten_list.append(item)
            
    return flatten_list



nested = [1, [2, 3], [4, [5, 6]], 7]
print(recursive_list(nested))