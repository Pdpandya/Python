original_list = [1, 2, 3, 4, 2, 3, 5, 6, 6]

# Remove duplicates by converting to set and back to list
list = list(set(original_list))

print("Original list:", original_list)
print("List after removing duplicates:", list)
