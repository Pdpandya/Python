dict = {'a': 100, 'b': 200, 'c': 50, 'd': 300, 'e': 150}

sitems = sorted(dict.items(), key=lambda x: x[1], reverse=True)
values = sitems[:3]

print("Highest 3 values:")
for key, value in values:
    print(key, ":", value)
