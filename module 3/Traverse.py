dict = {'a': 1, 'b': 2, 'c': 3}

for key in dict:
    print(key, ':', dict[key])

for key, value in dict.items():
    print(key, ':', value)

for key in dict.keys():
    print(key, ':', dict[key])

for value in dict.values():
    print(value)
