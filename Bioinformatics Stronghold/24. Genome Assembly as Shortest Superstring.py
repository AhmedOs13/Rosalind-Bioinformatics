def overlap(a, b):
    max_overlap = 0
    min_length = min(len(a), len(b))

    for i in range(1, min_length + 1):
        if a[-i:] == b[:i]:
            max_overlap = i

    return max_overlap


def merge(a, b, overlap_len):
    return a + b[overlap_len:]


def shortest_superstring(dna_strands):
    # Precompute overlap lengths for all pairs
    overlap_matrix = {}
    n = len(dna_strands)

    for i in range(n):
        for j in range(n):
            if i != j:
                overlap_matrix[(i, j)] = overlap(dna_strands[i], dna_strands[j])

    while len(dna_strands) > 1:
        max_overlap = -1
        best_pair = (0, 0)
        best_merged = ""

        for i in range(len(dna_strands)):
            for j in range(len(dna_strands)):
                if i != j:
                    overlap_len = overlap_matrix[(i, j)]
                    merged = merge(dna_strands[i], dna_strands[j], overlap_len)
                    if overlap_len > max_overlap:
                        max_overlap = overlap_len
                        best_pair = (i, j)
                        best_merged = merged

        i, j = best_pair
        # Remove the used strands and add the merged strand
        dna_strands[i] = best_merged
        del dna_strands[j]

        # Update overlap matrix for new pairs
        overlap_matrix = {}
        for k in range(len(dna_strands)):
            for l in range(len(dna_strands)):
                if k != l:
                    overlap_matrix[(k, l)] = overlap(dna_strands[k], dna_strands[l])

    return dna_strands[0]


# Read DNA strands from file
def read_dna_strands(file_path):
    with open(file_path) as file:
        lines = file.readlines()
    dna_strands = []
    dna_string = ''
    for line in lines:
        if line[0] == '>':
            if dna_string:
                dna_strands.append(dna_string)
                dna_string = ''
        else:
            dna_string += line.strip()
    if dna_string:
        dna_strands.append(dna_string)
    return dna_strands

file_path = input('>> ')
dna_strands = read_dna_strands(file_path)

# Find and print the shortest superstring
result = shortest_superstring(dna_strands)
print(result)
