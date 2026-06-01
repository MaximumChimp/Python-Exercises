#PROBLEM: Write a function to check if a full sentence is a palindrome. You must ignore case, spaces, and all punctuation marks.
#PURPOSE: Real-world palindromes often include punctuation (e.g., “Madam, I’m Adam”). This exercise teaches you how to sanitize data using isalnum() (is alphanumeric) before performing logic, ensuring your algorithm only focuses on the relevant characters.

def check_palindrom_sentence(text):
    cleaned_text = "".join(word.lower() for word in text if word.isalnum())
    
    return cleaned_text == cleaned_text[::-1]

result = check_palindrom_sentence("Madam, I'm Adam")

print(result)
