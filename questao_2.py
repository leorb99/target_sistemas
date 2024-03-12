def fibonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    fib = fibonacci(n-1)
    next = fib[-2] + fib[-1]
    if next <= n:
        fib.append(next)
    return fib

def is_fib(n):
    fib = fibonacci(n)
    if n in fib:
        return True
    return False

print(is_fib(55))
print(is_fib(78))
print(is_fib(89))
print(is_fib(1))
print(is_fib(4))