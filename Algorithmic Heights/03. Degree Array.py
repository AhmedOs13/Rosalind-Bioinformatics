def degree_array(array, degrees):
    degrees[array[0] - 1] += 1
    degrees[array[1] - 1] += 1
    return degrees


with open('test.txt') as f:
    lines = f.readlines()
    n, _ = map(int, lines[0].strip().split())
    degrees = [0 for _ in range(n)]
    for line in lines[1:]:
        array = list(map(int, line.strip().split()))
        degrees = degree_array(array, degrees)

print(*degrees)
