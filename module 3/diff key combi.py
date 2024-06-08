data = {'1': ['a', 'b'], '2': ['c', 'd']}
combinations = []

for key in data:
    for letter in data[key]:
        for other_key in data:
            if other_key != key:
                for other_letter in data[other_key]:
                    combinations.append(letter + other_letter)

print(" ".join(combinations))
