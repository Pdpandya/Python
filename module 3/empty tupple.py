list = [(1, 2), (), (3, 4), (), ()]
empty = []

for t in list:
    if t:
        empty.append(t)

print("List of tuples with empty tuples:", list)
print("List after removing empty tuples:", empty)
