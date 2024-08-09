def dna_to_rna(dna_sequence, start=0, end=None):
    if end is None:
        end = len(dna_sequence)
    segment = dna_sequence[start:end]
    rna_segment = segment.replace('T', 'U')

    return rna_segment


dna_sequence = input('Enter a DNA sequence: ').upper()
rna_sequence = dna_to_rna(dna_sequence)
print(rna_sequence)
