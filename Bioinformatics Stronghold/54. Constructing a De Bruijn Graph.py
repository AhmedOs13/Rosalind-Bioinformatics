with open('test.txt') as f:
    lines = f.readlines()
    s = set(line.strip() for line in lines)
    s_rc = set()
comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
for dna in s:
    dna_comp = str()
    dna_revcomp = str()
    for c in dna:
        dna_comp += comp.get(c, '?')
        dna_revcomp = dna_comp[::-1]
    s_rc.add(dna_revcomp)
all_strands = s | s_rc
result = list()
for dna in all_strands:
    result.append((dna[:-1], dna[1:]))
