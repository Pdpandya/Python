list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]

set1 = set(list1)
set2 = set(list2)

if set1.intersection(set2):
    result = True
else:
    result = False

print("one common member?", result)
