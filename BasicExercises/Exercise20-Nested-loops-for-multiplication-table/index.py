#PROBLEM: Print a multiplication table from 1 to 10 in a formatted grid.
#PURPOSE: To master “Matrix Generation.” This builds on the nested loop concepts from Exercise 8 and applies them to generate a structured data table. This is essential for understanding how to populate 2D arrays or generate spreadsheets.

for i in range(1,11):
    for j in range(1,11):
        print(i*j,end="\t")
    print("\n")