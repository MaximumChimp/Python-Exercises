#PROBLEM: Write a function that merges two dictionaries. If a key exists in both dictionaries, sum their values. If a key exists in only one, include it as is.
#PURPOSE: Real-world data often comes from multiple sources. Simply using dict.update() would overwrite duplicate keys. This exercise introduces you to efficient dictionary iteration and the dict.get(key, default) method, which is essential for avoiding KeyError.

def dict_merge(a,b):
    result = a.copy()

    for key,value in b.items():
        result[key] = result.get(key,0) + value
    return result

dict_a = {'a': 10, 'b': 20} 
dict_b = {'b': 5, 'c': 15}

merged = dict_merge(dict_a,dict_b)
print(f"Merged Dictionary: {merged}")
