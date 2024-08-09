def count_nucleotides(dna_sequence, start=0, end=None):
    if end is None:
        end = len(dna_sequence)
    segment = dna_sequence[start:end]

    count_a = segment.count('A')
    count_c = segment.count('C')
    count_g = segment.count('G')
    count_t = segment.count('T')

    return count_a, count_c, count_g, count_t


dna_sequence = input("Enter DNA sequence: ").upper()
a, c, g, t = count_nucleotides(dna_sequence)
print(a, c, g, t)
