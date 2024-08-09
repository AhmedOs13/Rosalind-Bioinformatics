start, end = map(int, input().split())
sum = 0

for i in range(start, end + 1):
    if i % 2 == 1:
        sum += i

print(sum)
