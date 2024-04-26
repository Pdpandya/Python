list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]

# Convert lists to sets for faster membership checking
set1 = set(list1)
set2 = set(list2)

# Check if there is any common element between the two sets
if set1.intersection(set2):
    result = True
else:
    result = False

print("Do the lists have at least one common member?", result)
