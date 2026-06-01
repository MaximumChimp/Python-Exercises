#PROBLEM: Write a program to capitalize the first letter of each word in a given string without using the built-in .title() method.
#PURPOSE: In this exercise, you will learn about “Tokenization” and “String Re-assembly.” You will split a sentence into words, change them, and then put the sentence back together. This helps you practice working with complex data structures.

def capitalize_first_letter(text):
    splitted_text = text.split(" ")
    new_text_list = []
    for word in splitted_text:
        new_word = word.capitalize()
        new_text_list.append(new_word)
    result = " ".join(new_text_list)
    print(result)
    
capitalize_first_letter("hello world from python")