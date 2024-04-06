# Taking user input for the string
string = input("Enter a string: ")

# Initializing an empty dictionary to store character frequencies
f = {}

# Counting the character frequencies
for char in string:
    if char in f:
        f[char] += 1
    else:
        f[char] = 1

print("Character frequencies in the string is")
for char, count in f.items():
    print(char , ": " ,str(count))
