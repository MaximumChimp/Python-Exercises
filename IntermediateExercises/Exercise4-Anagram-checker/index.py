#PROBLEM: Write a function that determines if two strings are anagrams (contain the exact same characters in a different order).
#PURPOSE: This problem introduces the concept of algorithmic sorting as a comparison tool. It demonstrates that transforming data into a “canonical” or “standard” form (sorted) makes comparison trivial.
def anagram_checker(word1,word2):
    sorted_word1 = sorted(word1)
    sorted_word2 = sorted(word2)

    if sorted_word1 == sorted_word2:
        print(f"Is {word1} an anagram of {word2}? True")
    else:
        print(f"Is {word1} an anagram of {word2}? False")
word1 = "listen" 
word2 = "silent"

anagram_checker(word1,word2)