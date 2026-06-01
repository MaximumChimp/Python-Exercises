#PROBLEM : Create a new list from two given lists such that the new list contains odd numbers from the first list and even numbers from the second list.

#SOLUTION 1


new_list = []
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
for i in list1:
    if i % 2 !=0:
        new_list.append(i)

for i in list2:
    if i % 2 == 0:
        new_list.append(i)
print(new_list)