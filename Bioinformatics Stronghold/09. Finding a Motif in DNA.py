def motif(dna_sequence, segment):
    index = []
    length = len(segment)
    for i in range(len(dna_sequence)):
        if dna_sequence[i:i+length] == segment:
            index.append(i+1)

    return index

dna_sequence = input()
segment = input()
print(*motif(dna_sequence, segment))
