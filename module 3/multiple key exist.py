# Sample dictionary
dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Keys to check
keys = {'a', 'b', 'e'}

# Find the intersection of keys in the dictionary and keys to check
intersection = keys.intersection(dict.keys())

# Check if the intersection contains all keys to check
if intersection == keys:
    print("All keys exist in the dictionary.")
else:
    print("At least one key does not exist in the dictionary.")
