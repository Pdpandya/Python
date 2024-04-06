# Taking user input
a = str(input("Enter a letter: "))

# Checking if the letter is a vowel
if a.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("The letter", a, "is a vowel.")
else:
    print("The letter", a , "is not a vowel.")
