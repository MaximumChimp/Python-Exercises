#PROBLEM:  Write a function that generates the Power Set of a given set (a set of all possible subsets, including the empty set and the set itself).
#PURPOSE:  Generating power sets is a fundamental concept in Combinatorics and algorithm design (like solving the knapsack problem). This exercise introduces you to the itertools module, specifically combinations.

from itertools import combinations

def get_power_set(s):
    elements = list(s)
    power_set = []

    for r in range(len(elements)+1):
        for combo in combinations(elements,r):
            power_set.append(combo)
    return power_set
s = {1,2,3}
x = get_power_set(s)
print(x)