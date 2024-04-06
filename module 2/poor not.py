string = input("Enter a string: ")

# Finding the positions of 'not' and 'poor'
n = string.find('not')
p= string.find('poor')

# Checking conditions and modifying the string
if n != -1 and p != -1 and n< p:
    result = string[:p] + 'good' + string[p + 4:]
else:
    result = string

# Printing the result
print("Modified string:", result)
