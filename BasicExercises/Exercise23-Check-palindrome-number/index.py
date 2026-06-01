#PROBLEM : Write a program to check if a given number is a palindrome. A palindrome number remains the same when its digits are reversed (e.g., 121, 545).
#PURPOSE : This exercise teaches “Algorithmic Reversal.” While strings are easy to reverse in Python, reversing a number mathematically using the modulo (%) and floor division (//) operators deepens understanding of how integers are stored in memory and how to manipulate digits individually.


def check_palindrome(digits):
    reverse_num = 0
    temp = digits
    while temp > 0:
        last_digit = temp % 10
        reverse_num = (reverse_num * 10)  + last_digit
        temp = temp // 10

    if digits == reverse_num:
        print("Palindrome")
    else:
        print("Not Palindrome")

check_palindrome(121)