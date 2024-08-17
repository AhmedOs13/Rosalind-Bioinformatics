n = int(input())

result = 1
for i in range(n):
    result *= 2
    result %= 1000000

print(result)
