#PROBLEM : Write a script that takes a list containing duplicate items and returns a new list with only unique elements.
#PURPOSE : This exercise teaches “Data De-duplication.” In real-world data science, datasets are often “messy” with repeating entries. Mastering the conversion between Lists (which allow duplicates) and Sets (which do not) is the fastest way to clean data.

data = [1,2,2,3,4,4,4,5]


#SOLUTION 1
unique_data= []

for i in data:
    if i not in unique_data:
        unique_data.append(i)
print(unique_data)

#SOLUTION 2
print(list(set(data)))