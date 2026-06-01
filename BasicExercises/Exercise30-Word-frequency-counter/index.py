#PROBLEM:  Write a program that counts how many times each word appears in a given paragraph and stores these counts in a dictionary.
#PURPOSE: This is a classic “Natural Language Processing” (NLP) task. It teaches you how to map data to occurrences, which is the logic used by search engines to index web pages or by social media platforms to identify trending hashtags.


text = "apple banana apple cherry banana apple"

words = text.split(" ")

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1



