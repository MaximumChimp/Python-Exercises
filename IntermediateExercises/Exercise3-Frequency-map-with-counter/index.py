#PROBLEM: Create a function that takes a string and returns a count of how many times each character appears. Ignore spaces and make it case-insensitive.
#PURPOSE: While you could build a frequency map with a standard loop, Python’s collections module offers a specialized tool called Counter. This exercise teaches you to leverage the Standard Library to write less code while increasing performance.

from collections import Counter

def frequency_counter(text):

    text = Counter(text.lower().replace(" ",""))
    print(text)


text = "Python Programming"
frequency_counter(text)