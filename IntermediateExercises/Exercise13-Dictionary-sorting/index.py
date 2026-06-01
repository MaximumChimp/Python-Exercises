#PROBLEM: Given a list of dictionaries (representing employees), sort them based on their “salary” in descending order using a lambda function.
#PURPOSE: In data processing, you rarely sort simple lists of numbers. You almost always sort “objects” (dictionaries). This exercise teaches you how to use the key parameter in Python’s sort() to target specific fields within a complex structure.


def sorted_dict(items):
    return sorted(items, key=lambda x:x["salary"],reverse = True)

employees = [{"name": "A", "salary": 50}, {"name": "B", "salary": 70}, {"name": "C", "salary": 60}]

lst = sorted_dict(employees)

print(lst)