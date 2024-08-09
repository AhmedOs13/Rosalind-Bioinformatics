# Codon dictionary for DNA to amino acid conversion
dna_codon = {'TTT': 'F', 'TCT': 'S', 'TAT': 'Y', 'TGT': 'C', 'TTC': 'F', 'TCC': 'S', 'TAC': 'Y', 'TGC': 'C',
             'TTA': 'L', 'TCA': 'S', 'TAA': '', 'TGA': '', 'TTG': 'L', 'TCG': 'S', 'TAG': '', 'TGG': 'W',
             'CTT': 'L', 'CCT': 'P', 'CAT': 'H', 'CGT': 'R', 'CTC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R',
             'CTA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R', 'CTG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R',
             'ATT': 'I', 'ACT': 'T', 'AAT': 'N', 'AGT': 'S', 'ATC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S',
             'ATA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R', 'ATG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R',
             'GTT': 'V', 'GCT': 'A', 'GAT': 'D', 'GGT': 'G', 'GTC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G',
             'GTA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G', 'GTG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G'}

# Read the entire file at once
file_path = input('>> Enter file path: ')
with open(file_path) as file:
    dna = ''
    intron = ''
    introns = []
    lines = file.readlines()

    is_dna = False
    for line in lines:
        if line[0] == '>':
            if not dna:
                is_dna = True
            else:
                is_dna = False
                if intron != '':
                    introns.append(intron)
                    intron = ''
        else:
            if is_dna:
                dna += line.strip()
            else:
                intron += line.strip()
    if intron != '':
      introns.append(intron)


# Remove introns from DNA sequence
for intron in introns:
    dna = dna.replace(intron, '')

# Translate DNA to protein
protein = ''.join(dna_codon.get(dna[i:i+3], '?') for i in range(0, len(dna), 3))

print(protein)
