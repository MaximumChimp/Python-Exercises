#PROBLEM: Given a list of strings, use a single list comprehension to extract strings that meet two criteria: they must be longer than 5 characters AND they must start with a vowel (a, e, i, o, u).
#PURPOSE: This exercise builds “filter stacking” skills. In professional Python development, you often need to perform complex data extraction in a readable, concise way without writing multiple if statements.

lst = ["apple", "education", "ice", "ocean", "python", "umbrella"]

new_list = [item for item in lst if len(item) > 5 and item[0].lower() in "aeiou" ]

print(new_list)
