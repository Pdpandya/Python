dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
keys = {'a', 'b', 'e'}

intersection = keys.intersection(dict.keys())

if intersection == keys:
    print("All keys exist in the dictionary.")
else:
    print(" key does not exist in the dictionary.")
