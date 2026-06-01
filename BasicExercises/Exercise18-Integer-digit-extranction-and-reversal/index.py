#PROBLEM :  Write a program to extract each digit from an integer in the reverse order.
#PURPOSE : This exercise explores “Mathematical Parsing.” Instead of converting a number to a string, use the modulo operator (%) and floor division (//) to isolate digits. This is common in low-level programming and algorithm challenges where type conversion is restricted.

number = 7536
temp = number
reverse_number = 0

while temp > 0:
    last_digit = temp % 10
    reverse_number = (reverse_number * 10) + last_digit
    temp = temp //10
print(reverse_number)


