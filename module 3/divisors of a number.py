num = int(input("Enter a number: "))
num = 0

for i in range(1, num + 1):
    if num % i == 0:
        sum += i

print("The sum of all divisors of num is:", sum)
