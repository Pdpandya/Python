# Input value
number = 28

# Sum of proper divisors
divisors = 0

# Find divisors and add them to the sum
for i in range(1, number):
    if number % i == 0:
        divisors += i

# Check if the sum of divisors equals the number
is_perfect = divisors == number

# Print the result
if is_perfect:
    print(number ,"is a perfect number.")
else:
    print(number, "is not a perfect number.")
