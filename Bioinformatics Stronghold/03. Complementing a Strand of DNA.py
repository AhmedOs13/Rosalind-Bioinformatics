def dna_complement(dna_sequence, start=0, end=None):
    if end == None:
        end = len(dna_sequence)

    segment = dna_sequence[start:end].upper()
    dna_comp = ''
    for char in segment:
        if char == 'A':
            dna_comp += 'T'
        elif char == 'G':
            dna_comp += 'C'
        elif char == 'T':
            dna_comp += 'A'
        elif char == 'C':
            dna_comp += 'G'
        else:
            dna_comp += '?'

    return dna_comp


dna_sequence = input('Enter a DNA sequence: ')
dna_comp = dna_complement(dna_sequence)
dna_comp_reverse = dna_comp[::-1]
print(dna_comp_reverse)
