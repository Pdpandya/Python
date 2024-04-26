# Original list with duplicate values
list = [1, 2, 3, 4, 2, 3, 5, 6, 6]

# Convert the list to a set to remove duplicates
values = set(list)

# Convert the set back to a list to maintain the original order
unique_values = values

# Output the result
print("Original list:", list)
print("Unique values:", unique_values)
