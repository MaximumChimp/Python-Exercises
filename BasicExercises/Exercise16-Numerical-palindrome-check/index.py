#PROBLEM : Write a program to check if a given number is a palindrome (reads the same forwards and backwards).
#PURPOSE : This exercise introduces the idea of “Reversing Logic.” Reversing a string is simple, but reversing an integer takes some math, like using division and modulo, or changing its type. This shows how data types can work differently.


number = 121

#SOLUTION 1
if str(number) == str(number)[::-1]:
    print(True)
else:
    print(False)
