string = input("Enter a string: ")

# Checking conditions and modifying the string accordingly
if len(string) >= 3:
    if string.endswith('ing'):
        result = string + 'ly'
    else:
        result = string + 'ing'
else:
    result = string

# Printing the result
print("Modified string:", result)
