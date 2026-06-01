#PROBLEM: Ask the user for a sentence. Replace every empty space in that sentence with an underscore (_) and print the final result.
#PURPOSE: This exercise focuses on “String Sanitization.” In web development and file management, spaces are often problematic (especially in URLs or file paths). Learning to replace characters is a critical skill for preparing data for storage or transmission.

user_sentence = input("Enter a sentence: ")

sanitized_sentence = user_sentence.replace(" ","_")

print(sanitized_sentence)