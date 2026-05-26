#PROBLEM : Write a program that calculates the factorial of a given number (e.g., 5!) using a for loop.
#PURPOSE : This exercise explores “Mathematical Accumulation.” A factorial (e.g., 5! = 5*4*3*2*1) requires you to maintain a running product across multiple iterations, which is a core pattern in scientific computing.

n = 5 
factorial = 1
for i in range(1,n+1):
    factorial *= i 

print(f"The factorial of {n} is {factorial}")
