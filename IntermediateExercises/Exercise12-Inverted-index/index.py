#PROBLEM: Create a function that “inverts” a dictionary. Convert a dictionary of Author: [List of Books] into a dictionary of Book: Author.
#PURPOSE: This is the logic behind how search engines work! An Inverted Index allows you to search for a term (the book) and immediately find where it belongs (the author). It emphasizes the use of nested loops and dictionary assignment.

def inverted_index(dict):
    new_dict = {}
    for key,value in dict.items():
        if isinstance(value, list):
            for item in value:
                new_dict[item] = key
    return new_dict

dict = {"Orwell": ["1984", "Animal Farm"], "Huxley": ["Brave New World"]}
print(inverted_index(dict))