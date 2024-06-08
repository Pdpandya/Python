input_string = "sure we are"
char_count = {}

for char in input_string:
    if char != ' ':
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

final_dict = {str(count): count for count in char_count.values()}

print(final_dict)
