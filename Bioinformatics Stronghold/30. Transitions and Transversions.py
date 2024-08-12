file_path = 'test.txt'
with open(file_path) as txt:
    dna = []
    string = ''
    lines = txt.readlines()
    for line in lines:
        if line.startswith('>'):
            if string:
                dna.append(string)
                string = ''
        else:
            string += line.strip()

    if string:
        dna.append(string)

transition = 0
transversion = 0
transition_pairs = [('A', 'G'), ('G', 'A'), ('C', 'T'), ('T', 'C')]

n = len(dna[0])
for i in range(n):
    if dna[0][i] != dna[1][i]:
        if (dna[0][i], dna[1][i]) in transition_pairs:
            transition += 1
        else:
            transversion += 1


print(transition / transversion)
