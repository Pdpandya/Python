# Taking user input
user_input = int(input("Enter a number: "))

result = 1
for i in range(2, user_input + 1):
    result *= i
print("The factorial of", user_input, "is:", result)

