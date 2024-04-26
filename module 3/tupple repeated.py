# Tuple to find repeated items
my_tuple = (1, 2, 2, 3, 4, 4, 4, 5, 5)

# empty set to store seen items
seen = set()

# empty list to store repeated items
repeated_items = []

# Iterate through the tuple
for item in my_tuple:
    # Check if the item has been seen before
    if item in seen:
        # add it to the list of repeated items
        repeated_items.append(item)
    else:
       # add it to the set of seen items
        seen.add(item)

# Output the repeated items
print("Tuple:", my_tuple)
print("Repeated items:", repeated_items)
