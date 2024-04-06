r = int(input("Enter the range for Fibonacci series: "))
a, b = 0, 1

fib_series = [a, b]
for i in range(r - 2): 
    a, b = b, a + b
    fib_series.append(b)

print("Fibonacci series within the given range:")
print(fib_series)

