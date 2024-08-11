def permutations(n, k):
    result = 1
    for i in range(n-k+1,n+1):
        result *= i
        result %= 1000000
    return result


n, k = map(int, input('>> ').split())
perm = permutations(n, k)
print(perm)
