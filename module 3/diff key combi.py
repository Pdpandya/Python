# Sample dictionary
data = {'1': ['a', 'b'], '2': ['c', 'd']}

# Initialize an empty list to store combinations
combinations = []

# Iterate over the values of the dictionary
for key in data:
    # Iterate over each letter in the current key's list
    for letter in data[key]:
        # Iterate over the values of the dictionary excluding the current key
        for other_key in data:
            if other_key != key:
                # Append the combination of letters to the list
                for other_letter in data[other_key]:
                    combinations.append(letter + other_letter)

# Join the combinations into a single string and print
print(" ".join(combinations))
