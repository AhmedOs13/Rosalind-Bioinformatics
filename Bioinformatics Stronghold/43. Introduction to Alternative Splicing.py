import math


def nCr(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


n, k = map(int, input().split())

total_number_of_subsets = 0
MOD = 1000000

for i in range(k, n + 1):
    total_number_of_subsets += nCr(n, i)
    total_number_of_subsets %= MOD

print(total_number_of_subsets)
