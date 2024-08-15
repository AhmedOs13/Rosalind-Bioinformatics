def compute_matching(strand):
    A = strand.count('A')
    U = strand.count('U')
    C = strand.count('C')
    G = strand.count('G')

    result = partial_factorial(max(A, U), min(A, U)) * partial_factorial(max(C, G), min(C, G))
    return int(result)


def partial_factorial(n, r):
    product = 1
    for i in range(n - r, n):
        product *= (i + 1)
    return product


file_path = 'test.txt'
with open(file_path) as txt:
    lines = txt.readlines()
    rna = ''.join(lines[i].strip() for i in range(1, len(lines)))

total_matching = compute_matching(rna)
print(total_matching)
