# Input a nonnegative integer
num = int(input("Enter a nonnegative integer: "))

# Check if the input is a nonnegative integer
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("Factorial of 0 is 1.")
else:
    # Calculate factorial using iteration
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print("Factorial of", num, "is", factorial)
