#PROBLEM: Write a program to check if a user-entered string contains any numeric digits. Use a for loop to examine each character.
#PURPOSE: This exercise will help you learn about string traversal and character analysis. In software development, these skills are important for tasks like checking if a username has forbidden characters or if a password is complex enough.

def digit_detection(text):
    for char in text:
        if char.isdigit():
            print(f"The string '{text}' contains digits")
            break
    else:
        print(f"The string '{text}' does not contains digits")

digit_detection("Python")