codon_dict = {
    'UUU': 'F', 'UCU': 'S', 'UAU': 'Y', 'UGU': 'C',
    'UUC': 'F', 'UCC': 'S', 'UAC': 'Y', 'UGC': 'C',
    'UUA': 'L', 'UCA': 'S', 'UAA': '-', 'UGA': '-',
    'UUG': 'L', 'UCG': 'S', 'UAG': '-', 'UGG': 'W',
    'CUU': 'L', 'CCU': 'P', 'CAU': 'H', 'CGU': 'R',
    'CUC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R',
    'CUA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R',
    'CUG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R',
    'AUU': 'I', 'ACU': 'T', 'AAU': 'N', 'AGU': 'S',
    'AUC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S',
    'AUA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R',
    'AUG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R',
    'GUU': 'V', 'GCU': 'A', 'GAU': 'D', 'GGU': 'G',
    'GUC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G',
    'GUA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G',
    'GUG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G'
}

# Reading file (txt)
file_path = input("Enter the file path:")
dna_string = ''
with open(file_path) as fasta:
    lines = fasta.readlines()
    for line in lines:
        line = line.strip()
        if line[0] == '>':
            pass
        else:
            dna_string += line

# Reverse Complement function
def reverseComplement(rna_string):
    rev_string = ''
    for char in rna_string:
        if char == 'A':
            rev_string += 'U'
        elif char == 'U':
            rev_string += 'A'
        elif char == 'G':
            rev_string += 'C'
        elif char == 'C':
            rev_string += 'G'

    string = rev_string[::-1]
    return string

# RNA-Protein Conveter
def rna_to_protein(rna_string):
    string = ''
    for i in range(0, len(rna_string) - 3):
        codon = rna_string[i:i + 3]
        string += codon_dict.get(codon, '?')

    return string

# ORF Function
def orf_protein(string):
    prot_str = []
    result = ''
    for i in range(len(string)):
        if string[i] == 'M':
            for j in range(i, len(string), 3):
                if string[j] != '-':
                    result += string[j]
                else:
                    if result in prot_str:
                        pass
                    else:
                        prot_str.append(result)
                    result = ''
                    break
    return prot_str

# ORF for rormal RNA
rna_string = dna_string.replace('T', 'U')
protein_string = rna_to_protein(rna_string)
orf_norm = orf_protein(protein_string)

# ORF for RevComp Rna
rev_comp = reverseComplement(rna_string)
prot_rev = rna_to_protein(rev_comp)
orf_rev = orf_protein(prot_rev)

# Merging them together in [final_orf]
final_orf = list()
for string in orf_rev:
    final_orf.append(string)
for string in orf_norm:
    if string in orf_rev:  pass
    else:  final_orf.append(string)

# Final ORF Result
for string in final_orf:
    print(string)
