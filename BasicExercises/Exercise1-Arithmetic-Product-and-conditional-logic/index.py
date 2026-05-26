#PROBLEM: Write a Python function that accepts two integer numbers. 
        #If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.

#PURPOSE: Learn basic control flow and the use of if-else statements. Understand how code decisions change output based on a mathematical threshold.

def ArithmeticProduct(a,b):
    product = a * b
    if product < 1000:
        return product
    else:
        return a + b
    
result = ArithmeticProduct(20,30)
print('The result is {}'.format(result))

result = ArithmeticProduct(40,30)
print('The result is {}'.format(result))