#PROBLEM: Create a function rotate_list(lst, n, direction) that shifts the elements of a list by N positions. The direction can be ‘left’ or ‘right’.
#PURPOSE: List rotation is common in cryptography and UI carousels. This exercise teaches you how to use slicing and the modulo operator to handle shifts that are larger than the list length.

def rotate_list(lst,n,direction):
    if not lst:
        return lst

    n = n % len(lst)

    if direction == 'right':
        return lst[-n:] + lst[:-n]
    else:
        return lst[n:] + lst[:n]

test1 = rotate_list([1,2,3,4,5],2,'left')
test2 = rotate_list([1,2,3,4,5],2,'right')
print(test1)
print(test2)