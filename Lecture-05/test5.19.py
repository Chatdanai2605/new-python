def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(6))  #output : 8