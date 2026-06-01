#PROBLEM: Merge two dictionaries. If they share a key, the new dictionary should store a list containing values from both dictionaries instead of overwriting the first one.
#PURPOSE: Standard dictionary merging (dict.update()) overwrites data. This exercise teaches you how to “preserve” data during a merge, which is essential when combining user settings or merging search results from different sources.

def merge_dict(d1,d2):
    combined = {}

    all_keys = set(d1.keys()) | set(d2.keys())

    for key in all_keys:
        values = []
        if key in d1:
            values.append(d1[key])
        if key in d2:
            values.append(d2[key])
       
        combined[key] = values
        print(combined[key])
    # return combined

d1 = {"a": 1, "b": 2} 
d2 = {"b": 3, "c": 4}

print(f"Grouped Merge: {merge_dict(d1, d2)}")