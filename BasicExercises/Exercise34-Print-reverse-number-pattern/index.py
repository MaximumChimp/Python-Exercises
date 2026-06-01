#PROBLEM: Print a downward number pattern where each row starts with a decreasing value.
#PURPOSE: In this exercise, you will learn about range control and practice using negative steps in loops to move backwards. This skill is important for algorithms that process data from the end of a file to the beginning.

def reverse_pattern(n):
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print(j,end=" ")
        print()
        
reverse_pattern(5)