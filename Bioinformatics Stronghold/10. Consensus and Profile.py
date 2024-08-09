import numpy as np

# Read txt file
motifs = []
file_path = input("Enter the path of the file: ")
with open(file_path) as test:
    lines = test.readlines()
    dna_string = ''
    for i in range(0, len(lines)):
        s = lines[i].strip()
        if s[0] == '>':
            motifs.append(dna_string)
            dna_string = ''
        else:
            dna_string += s
motifs.append(dna_string)
motifs = motifs[1:]

# Building the matrix
str_len = len(motifs[0])
genome = [[0] * str_len for _ in range(4)]
print(genome)

# Fill the matrix
for line in motifs:
    for i, char in enumerate(line):
        if char.upper() == 'A':
            genome[0][i] += 1
        elif char.upper() == 'C':
            genome[1][i] += 1
        elif char.upper() == 'G':
            genome[2][i] += 1
        elif char.upper() == 'T':
            genome[3][i] += 1

# Consensus string
string=''

for i in range(len(genome[0])):
    column = [genome[j][i] for j in range(len(genome))]
    max_index = np.argmax(column)
    match max_index:
        case 0: string += 'A'
        case 1: string += 'C'
        case 2: string += 'G'
        case 3: string += 'T'

# Final submission
print(string)
print('A:', *genome[0])
print('C:', *genome[1])
print('G:', *genome[2])
print('T:', *genome[3])

