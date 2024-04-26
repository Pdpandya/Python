# Sample dictionary
dict = {'a': 100, 'b': 200, 'c': 50, 'd': 300, 'e': 150}

# Sort the dictionary items based on values in descending order
sorted_items = sorted(dict.items(), key=lambda x: x[1], reverse=True)

# Get the highest 3 values
values = sorted_items[:3]

# Print the highest 3 values
print("Highest 3 values in the dictionary:")
for key, value in values:
    print(key, ":", value)
