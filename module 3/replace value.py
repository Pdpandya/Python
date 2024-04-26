# List of tuples
tuple_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

# New value to replace the last value in each tuple
new_value = 10

# Replace the last value of each tuple in the list
updated = [(t[:-1] + (new_value,)) for t in tuple_list]

# Output the updated list of tuples
print("Original list of tuples:", tuple_list)
print("Updated list of tuples:", updated)
