#PROBLEM:  Create a list of 5 words. Write a loop that iterates through the list and prints each word alongside its character count.
#PURPOSE:This exercise introduces “Metadata Extraction.” Often, you aren’t just interested in the data itself, but in its properties. In web development, this logic is used to validate if a user’s password or username meets specific length requirements.

words = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

for word in words:
    length = len(word)
    print(f"{word} - {length}")