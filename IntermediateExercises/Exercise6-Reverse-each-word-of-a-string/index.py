#PROBLEM: Given a sentence, reverse each individual word within the string while maintaining the original word order.
#PURPOSE: This exercise teaches you the difference between reversing a sequence (the whole string) and iterating through sub-sequences (words). It emphasizes the use of the .split() and .join() methods, which are essential for text processing.

def reverse_string(text):
    split_text = text.split(" ")
    new_text = []
    for word in split_text:
        reverse_word = word[::-1]
        new_text.append(reverse_word)
    reverse_text = " ".join(new_text)
    print(reverse_text)

reverse_string("Python is awesome")