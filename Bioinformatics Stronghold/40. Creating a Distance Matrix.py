def difference(s1, s2):
    length = len(s1)
    counter = 0
    for i in range(length):
        if s1[i] != s2[i]:
            counter += 1

    return counter / length


file_path = 'test.txt'
with open(file_path) as txt:
    lines = txt.readlines()
    dna = []
    string = ''
    for line in lines:
        if line.startswith('>'):
            if string:
                dna.append(string)
                string = ''
        else:
            string += line.strip()

    if string:
        dna.append(string)

n = len(dna)

matrix = [[0.0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        matrix[i][j] = difference(dna[i], dna[j])

for line in matrix:
    for i in range(len(line)):
        print(f'{line[i]:.5f}\t', end='')
    print()
