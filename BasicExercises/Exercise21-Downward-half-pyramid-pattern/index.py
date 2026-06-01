#PROBLEM:Print a downward half-pyramid pattern using stars (*).
#PURPOSE:Learn about reverse indexing. Controlling loop boundaries in reverse is important for algorithms that process data from end to beginning.

row = 5

for i in range(1,row+1):
    for j in range(1, row-i+2):
        print("*",end=" ")
    print()