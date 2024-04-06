string = input("Enter a string: ")

# Checking the length of the string
if len(string) < 2:
    result = ""
else:
    # Creating a string with the first 2 and last 2 characters
    result = string[:2] + string[-2:]

# Printing the result
print("Result:", result)
