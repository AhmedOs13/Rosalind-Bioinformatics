def revComplement(strand):
    comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    comp_dna = ''.join(comp.get(base) for base in strand)
    return comp_dna[::-1]


def hammingDistance(strand1, strand2):
    count = 0
    n = len(strand1)
    for i in range(n):
        if strand1[i] != strand2[i]:
            count += 1
    return count

#  Open dataset file
file_path = input('>> ')
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

# Checking all possible strands (revComp or original strand)
possible = []
for strand in dna:
    possible.append(strand)
    possible.append(revComplement(strand))

# Count appearance of each strand
strand_counts = {}
for strand in possible:
    if strand in strand_counts:
        strand_counts[strand] += 1
    else:
        strand_counts[strand] = 1

# Divide them into correct and incorrect strands according to their appearance
correct = set()
incorrect = []

for strand in dna:
    if strand_counts[strand] > 1:
        correct.add(strand)
    else:
        incorrect.append(strand)

all_possible_correct = []
for strand in correct:
    all_possible_correct.append(strand)
    all_possible_correct.append(revComplement(strand))

# Try to find the closest match with 1 Hamming Distance
corrected_dna = {}
for incor_dna in incorrect:
    for poss_dna in all_possible_correct:
        if hammingDistance(incor_dna, poss_dna) == 1:
            corrected_dna[incor_dna] = poss_dna
            break

# Print as required
for key, value in corrected_dna.items():
    print(f'{key}->{value}')

