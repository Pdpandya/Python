# Two dictionaries
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

# Combined dictionary with summed values for common keys
combine = {}

# Add values from d1
for key, value in d1.items():
    combine[key] = value

# Add values from d2, summing up values for common keys
for key, value in d2.items():
    if key in combine:
        combine[key] += value
    else:
        combine[key] = value

# Print the resulting dictionary
print("Combined dictionary :", combine)
