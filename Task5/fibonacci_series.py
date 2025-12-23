fib = lambda n: [0, 1] if n == 2 else fib(n-1) + [fib(n-1)[-1] + fib(n-1)[-2]]

print("Fibonacci series of the given number is:",fib(5))