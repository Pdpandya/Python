# List of tuples with empty tuples
list = [(1, 2), (), (3, 4), (), (), (5,), (), (6, 7, 8), ()]

# Initialize an empty list to store non-empty tuples
empty = []

# Iterate through the list of tuples
for t in list:
    # Check if the tuple is not empty
    if t:
        # If not empty, append it to the list of non-empty tuples
        empty.append(t)

# Output the list after removing empty tuples
print("List of tuples with empty tuples:", list)
print("List after removing empty tuples:", empty)
