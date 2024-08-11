file_path = input('>> ')
with open(file_path) as f:
    dna = []
    lines = f.readlines()
    string = ''
    for line in lines:
        if line[0] != '>':
            string += line.strip()
        else:
            if string != '':
                dna.append(string)
                string = ''
if string:
    dna.append(string)

indices = []
i = 0
for c in dna[1]:
    i += dna[0][i:].index(c) + 1
    indices.append(i)

print(*indices)
