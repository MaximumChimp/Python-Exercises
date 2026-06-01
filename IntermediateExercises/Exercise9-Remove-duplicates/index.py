#PROBLEM: Write a function that removes duplicate elements from a list. You cannot use set() because sets do not maintain the original order of elements.
#PURPOSE: While list(set(items)) is the fastest way to get unique items, it scrambles the order. This exercise teaches you how to use an auxiliary “seen” collection to maintain sequence integrity, a common requirement in data logging.

def remove_duplicates(lst):
    result = []
    seen = set()

    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

x = remove_duplicates([1, 2, 2, 3, 1, 4, 2])
print(x)


