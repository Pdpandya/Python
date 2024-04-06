string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Swapping the first two characters of each string
string = string2[:2] + string1[2:] + ' ' + string1[:2] + string2[2:]

# Printing the result
print("swap string is :",string)

