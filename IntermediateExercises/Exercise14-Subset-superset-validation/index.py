#PROBLEM: Write a script that takes two lists of integers from a user, converts them to sets, and determines if the first set is a Subset, a Superset, or Disjoint from the second.
#PURPOSE:  This exercise introduces formal relational logic between collections. Understanding these relationships is vital when managing user permissions (is this set of permissions a subset of the required ones?) or validating categories.

def validate_set(a,b):
    lst1 = set(a)
    lst2 = set(b)

    if lst1.issubset(lst2):
        print("Set A is a subset of Set B.")
    elif lst1.issuperset(lst2):
        print("Set A is a superset of Set B")

    if lst1.isdisjoint(list2):
        print("Set A is disjoint from Set B")
    else:
        print(f"The sets share these elements: {lst1 & lst2}")


list1 = [1,2,3]
list2 = [1,2,3,4,5]

validate_set(list1,list2)