#PROBLEM:  Iterate through the first 10 numbers (0–9). In each iteration, print the current number, the previous number, and their sum.
#PURPOSE: This exercise teaches “State Tracking.” In programming, you often need to remember a value from a previous loop iteration to calculate results in the current one. This is the basis for algorithms like Fibonacci sequences or running totals.

print("Printing current and previous number sum in a range(10)")

previous_num = 0 

for i in range(10):
    sum_num = previous_num + i
    print(" Current Number {} Previous Number {} Sum: {}".format(i,previous_num,sum_num))
    previous_num = i