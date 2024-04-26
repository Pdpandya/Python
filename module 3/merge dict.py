dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Merge dictionaries using dict() constructor and ** unpacking operator
merged_dict = dict(dict1, **dict2)

print("Merged dictionary using dict() constructor and ** unpacking operator:", merged_dict)
