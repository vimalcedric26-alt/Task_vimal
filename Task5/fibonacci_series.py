fib = lambda n: [0, 1] if n == 2 else fib(n-1) + [fib(n-1)[-1] + fib(n-1)[-2]]

print(fib(5))