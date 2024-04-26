string = "A man a plan a canal Panama".replace(" ", "").lower()
palindrome = string == string[::-1]

print(palindrome)  
