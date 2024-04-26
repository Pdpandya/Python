# Input number
num = int(input("Enter a number: "))

# Initialize sum
sum = 0

# Find divisors and add them to sum
for i in range(1, num + 1):
    if num % i == 0:
        sum += i

print("The sum of all divisors of num is:", sum)
