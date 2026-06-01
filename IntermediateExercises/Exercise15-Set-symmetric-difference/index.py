#PROBLEM: Given two lists of student IDs, find the IDs that appear in either the first or the second list, but not in both.
#PURPOSE: This is known as the Symmetric Difference. It is a powerful way to identify “exclusive” data. For example, finding customers who visited either in January or February, but did not visit in both months.

def symmetric_difference(a,b):
    result = []

    for item in a:
        if item not in b:
            if item not in result:
                result.append(item)
    
    for item in b:
        if item not in a:
            if item not in result:
                result.append(item)
    return set(result)


    #SOLUTION 2:
    #return set(a) ^ set(b)
lst1 = [101,102,103]
lst2 = [103,104,105]
x = symmetric_difference(lst1,lst2)
print(x)