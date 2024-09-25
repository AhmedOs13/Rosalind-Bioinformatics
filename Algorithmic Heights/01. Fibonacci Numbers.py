def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1

    a, b = 0, 1
    for i in range(1, n):
        c = a + b
        a, b = b, c

    return c


n = int(input())
print(fibonacci(n))
