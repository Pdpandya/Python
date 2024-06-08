list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
new = 10

for t in list:
    
    update= t[:-1] + (new,)


print("Original list of tuples:", list)
print("Updated list of tuples:",update )
