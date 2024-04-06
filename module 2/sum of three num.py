# Taking user input for three integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Checking if two values are equal
if num1 == num2 or num2 == num3 or num1 == num3:
    # If two values are equal, set sum to zero
    sum_of_integers = 0
else:
    # If no two values are equal, calculate the sum
    sum_of_integers = num1 + num2 + num3

# Printing the result
print("The sum is:", sum_of_integers)
