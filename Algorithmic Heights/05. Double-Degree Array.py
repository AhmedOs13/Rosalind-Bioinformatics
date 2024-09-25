def sum_of_neighbor_degrees(n, edges):
    adjacency_list = [[] for _ in range(n)]
    degree = [0] * n

    for u, v in edges:
        adjacency_list[u - 1].append(v - 1)
        adjacency_list[v - 1].append(u - 1)
        degree[u - 1] += 1
        degree[v - 1] += 1

    result = [0] * n
    for i in range(n):
        for neighbor in adjacency_list[i]:
            result[i] += degree[neighbor]

    return result


with open('test.txt') as f:
    lines = f.readlines()
    n, m = map(int, lines[0].strip().split())
    edges = [tuple(map(int, lines[i].strip().split())) for i in range(1, m+1)]
    result = sum_of_neighbor_degrees(n, edges)
    print(" ".join(map(str, result)))
