n, k = map(int, input().split())
a = 0
b = 1
result = 1
for i in range(n-1):
    result = a*k + b
    a = b
    b = result

print(result)
