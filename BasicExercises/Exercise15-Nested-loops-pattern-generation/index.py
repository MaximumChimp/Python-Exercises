#PROBLEM : Print the following pattern where each row contains a number repeated a specific number of times based on its value.
#PURPOSE : Pattern printing is a classic way to learn “Nested Loops.” You coordinate an outer loop for rows and an inner loop for columns or repetitions. This improves spatial logic and control over output formatting.
n = 5 

for i in range(n+1):
    for j in range(n-i+1):
        print(" ",end="")

    for k in range(1,2 * i):
        print("*",end="")
    print()

