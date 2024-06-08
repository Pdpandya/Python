m = (1, 2, 2, 3, 4, 4, 4, 5, 5)
s = set()
r = []

for item in m:
    if item in s:
        r.append(item)
    else:
        s.add(item)

print("Tuple:", m)
print("Repeated items:", r)
