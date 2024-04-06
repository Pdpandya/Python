string = input("Enter a string: ")

if len(string) % 4 == 0:
    # Reversing the string
    result = string[::-1]
else:
    result = string

print("Result:", result)

