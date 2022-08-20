def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    

# MAIN
print(fib(2))
print(fib(3))
print(fib(5))
print(fib(7))
print(fib(50))
print(fib(100))