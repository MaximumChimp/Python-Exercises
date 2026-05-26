#PROBLEM : Write a program that takes a string and reverses it (e.g., “Python” becomes “nohtyP”).
#PURPOSE : This exercise demonstrates “Sequence Slicing.” Strings in Python are sequences, and mastering the slicing syntax is a powerful shortcut for data manipulation that would take 5-10 lines of code in other languages.

text = 'Python'

reversed_text = text[::-1]

print(f"Original String: {text}")
print(f"reverse string: {reversed_text}")