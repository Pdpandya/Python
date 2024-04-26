# List of tuples to unzip
list = [(1, 'a'), (2, 'b'), (3, 'c')]

# Unzip the list of tuples into individual lists
unzipped_lists = (zip(*list))

# Output the unzipped lists
print("List of tuples:", list)
print("Unzipped lists:", unzipped_lists)
