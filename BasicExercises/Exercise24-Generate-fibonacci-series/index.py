#PROBLEM: Write a program to print the first 15 terms of the Fibonacci series. The sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones
#PURPOSE: e Fibonacci sequence is a classic way to learn about state management in loops. You keep track of two changing variables at once to find the next number, which helps you see how data moves through each step.

#SOLUTION 1: This return exact value only
def fibonacci(n):
    if n <= 1:
        return n
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7))

#SOLUTION 2

def fibonacci(n):
    num1,num2 = 0,1
    for i in range(n+1):
        print(num1, end=" ")
        result = num1 + num2
        num1 = num2
        num2 = result 
   
fibonacci(7)

