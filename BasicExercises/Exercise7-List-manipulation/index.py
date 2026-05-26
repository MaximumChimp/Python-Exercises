#PROBLEM : Create a list of 5 fruits. Add a new fruit to the end of the list, then remove the second fruit (at index 1).
#PURPOSE : This exercise teaches “Dynamic Collection Management.” Lists are rarely static; being able to modify, expand, and prune them is essential for handling data like shopping carts, user lists, or inventory systems.

fruits = ["apple","banana","cherry","date","elderberry"]

fruits.append("fig")
fruits.pop(1)
print(fruits)