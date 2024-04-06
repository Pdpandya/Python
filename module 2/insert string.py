string = input("Enter the main string: ")

string1 = input("Enter the string to insert: ")

# Calculating the middle index
m = len(string) // 2

# Creating the result string by inserting the string in the middle
result= string[:m] + string1 + string[m:]

# Printing the result
print("Result:", result)
