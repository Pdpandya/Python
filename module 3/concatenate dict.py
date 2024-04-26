# Define the dictionaries to concatenate
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

# Concatenate the dictionaries to create a new one
concatenated_dict = {**dict1, **dict2, **dict3}

# Output the concatenated dictionary
print("Concatenated dictionary:", concatenated_dict)
