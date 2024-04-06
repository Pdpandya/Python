list = input("Enter a list of words separated by spaces: ").split()

if not list:
    print("The list is empty.")
else:
    # Using the max function with key=len to find the longest word
    longest_word = max(list, key=len)

    # Printing the length of the longest word
    print("Length of the longest word:", len(longest_word))
