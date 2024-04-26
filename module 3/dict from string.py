# Sample string
input_string = "sure we are"

# Create an empty dictionary to store character counts
char_count = {}

# Iterate over each character in the string
for char in input_string:
    # If the character is not a space
    if char != ' ':
        # If the character is already in the dictionary, increment its count
        if char in char_count:
            char_count[char] += 1
        # If the character is not in the dictionary, add it with count 1
        else:
            char_count[char] = 1

# Convert count values to strings and create the final dictionary
final_dict = {str(count): count for count in char_count.values()}

# Print the resulting dictionary
print("Dictionary created from string with count of letters:")
print(final_dict)
