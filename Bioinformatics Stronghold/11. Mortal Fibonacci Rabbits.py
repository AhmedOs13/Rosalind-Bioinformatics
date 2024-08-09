n, m = map(int, input().split())

def population(n, m):
    parent = [0] * (n + m)
    child = [1] + [0] * (n + m - 1)
    parent[m] -= 1

    for i in range(0, n - 1):
        death = child[i]
        child[i + 1] = parent[i]
        parent[i + m + 1] -= child[i + 1]
        parent[i + 1] += death + parent[i]

    return parent[n - 1] + child[n - 1]


result = population(n, m)
print(result)
