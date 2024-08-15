file_path = 'test.txt'
with open(file_path) as txt:
    lines = txt.readlines()
    dna = ''
    for line in lines[1:]:
        dna += line.strip()

n = len(dna)
P = [0] * n

for k in range(1, n):
    j = P[k - 1]
    while j > 0 and dna[k] != dna[j]:
        j = P[j - 1]
    if dna[k] == dna[j]:
        j += 1
    P[k] = j

print(*P)
