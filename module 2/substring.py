
string = input("Enter a string: ")

substring = input("Enter the substring to count: ")

# Counting occurrences of the substring
count = string.count(substring)

# Printing the result
print("The substring " , substring , " occurs " , str(count) , " times.")