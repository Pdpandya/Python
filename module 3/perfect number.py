number = 28
divisors = 0

for i in range(1, number):
    if number % i == 0:
        divisors += i

is_perfect = divisors == number

if is_perfect:
    print(number ,"is a perfect number.")
else:
    print(number, "is not a perfect number.")
