dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

dict = dict(dict1, **dict2)

print("Merged dictionary:", dict)
