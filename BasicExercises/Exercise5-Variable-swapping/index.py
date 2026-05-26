#PROBLEM : Write a program to swap the values of two variables, a and b, without using a third temporary variable.
#PURPOSE : This exercise will help you learn about memory efficiency and Python’s special tuple unpacking feature. In other languages like C or Java, you need a temporary variable to swap values safely. In Python, you can swap values in one line without risking data loss.

a = 5 
b =10

print("Before Swapping a = {} b = {}".format(a,b))

a,b = b,a

print("After Swapping a = {} b = {}".format(a,b))

