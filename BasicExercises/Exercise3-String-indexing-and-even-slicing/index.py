#PROBLEM :  Display only those characters which are present at an even index number in given string.
#PURPOSE : Understand how data is stored in memory using zero-based indexing. In most languages, the first character is at position 0, the second at 1, and so on. Mastering indexing is vital for data parsing.


string  = "pynative"

#SOLUTION 1
for i in range(0,len(string)-1,2):
    print(string[i])

#SOLUTION 2
chars = string[::2]
for char in chars:
    print(char)