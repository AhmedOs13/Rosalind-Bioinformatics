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


def rna_to_protein(rna_sequence, start=0, end=None):

    protein_sequence = ''
    if end is None:
        end = len(rna_sequence)
    segment = rna_sequence.upper()

    protein_sequence = ''
    for i in range(start, end, 3):
        codon = segment[i:i + 3]
        if codon_dict.get(codon, '-') == '-':
            break
        if len(codon) == 3:
            protein_sequence += codon_dict.get(codon, '?')

    return protein_sequence


rna_sequence = input('Enter a RNA sequence: ')
protein_sequence = rna_to_protein(rna_sequence)
print(protein_sequence)
