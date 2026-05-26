#PROBLEM : Write a function to remove characters from a string starting from index 0 up to n and return a new string.
#PURPOSE : This exercise demonstrates how to truncate data strings, a common data-cleaning task.

def remove_chars(string,n):
    return string[n:]

print(remove_chars('pynative',4))
print(remove_chars('pynative',2))