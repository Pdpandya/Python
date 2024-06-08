d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
combine = {}

for key, value in d1.items():
    combine[key] = value

for key, value in d2.items():
    if key in combine:
        combine[key] += value
    else:
        combine[key] = value

print("Combined dictionary :", combine)
