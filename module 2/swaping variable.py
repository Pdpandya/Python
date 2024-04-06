# Swap two numbers with a temporary variable
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Before swapping: num1 =", num1, ", num2 =", num2)

# Using a temporary variable
temp = num1
num1 = num2
num2 = temp

print("After swapping with temp variable: num1 =", num1, ", num2 =", num2)




# Swap two numbers without a temporary variable
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Before swapping: num1 =", num1, ", num2 =", num2)

# Without using a temporary variable
num1, num2 = num2, num1

print("After swapping without temp variable: num1 =", num1, ", num2 =", num2)
