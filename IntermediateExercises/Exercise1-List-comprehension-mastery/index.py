#PROBLEM: Write a single-line list comprehension that takes a list of strings, filters out strings shorter than 4 characters, and converts the remaining strings to uppercase.
#PURPOSE:  List comprehensions are a hallmark of Pythonic code. They allow you to replace verbose for loops and .append() calls with a readable, optimized single line. This exercise teaches you how to combine transformation (uppercase) and filtering (length check) in one expression.

words = ["apple", "bat", "cherry", "dog", "elderberry"]

result = [word.upper() for word in words if len(word) >= 4]

print(result)