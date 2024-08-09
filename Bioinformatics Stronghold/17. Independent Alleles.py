from math import factorial

def combination(n, r):
    result = factorial(n) / (factorial(n - r) * factorial(r))
    return result

k, n = map(int, input().split())
organisms = 2 ** k

# Binomial Distribution
sum = 0
for i in range(n-1,organisms):
    sum += combination(organisms, i + 1) * (0.25) ** (i + 1) * (0.75) ** (organisms - i - 1)

result = round(sum, 3)
print(result)
