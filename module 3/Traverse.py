# Dictionary to traverse
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Traverse through the dictionary using a for loop
for key in my_dict:
    print(key, ':', my_dict[key])


# Traverse through the dictionary using the items() method
for key, value in my_dict.items():
    print(key, ':', value)


# Traverse through the dictionary using the keys() method
for key in my_dict.keys():
    print(key, ':', my_dict[key])


# Traverse through the dictionary using the values() method
for value in my_dict.values():
    print(value)
