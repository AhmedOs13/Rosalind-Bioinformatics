def pairwise_align(seq1, seq2):
    match_score = 2
    mismatch_score = 1
    gap_score = 0
    num_rows, num_cols = len(seq2) + 1, len(seq1) + 1

    # Initialize score matrix and direction matrix with list comprehensions
    score_matrix = [[0] * num_cols for _ in range(num_rows)]
    direction_matrix = [[0] * num_cols for _ in range(num_rows)]

    # Precompute gap penalties for first row and column
    for i in range(1, num_rows):
        score_matrix[i][0] = gap_score * i
        direction_matrix[i][0] = 1  # Up (deletion)

    for j in range(1, num_cols):
        score_matrix[0][j] = gap_score * j
        direction_matrix[0][j] = 2  # Left (insertion)

    # Fill the score matrix
    for i in range(1, num_rows):
        for j in range(1, num_cols):
            match = score_matrix[i - 1][j - 1] + (match_score if seq2[i - 1] == seq1[j - 1] else mismatch_score)
            delete = score_matrix[i - 1][j] + gap_score
            insert = score_matrix[i][j - 1] + gap_score

            # Choose the best score and update matrices
            score_matrix[i][j], direction_matrix[i][j] = max(
                (match, 0), (delete, 1), (insert, 2)
            )

    # Backtracking to get the aligned sequences
    aligned_seq1, aligned_seq2 = [], []
    i, j = num_rows - 1, num_cols - 1

    while i > 0 or j > 0:
        if direction_matrix[i][j] == 0:  # Diagonal (match/mismatch)
            aligned_seq1.append(seq1[j - 1])
            aligned_seq2.append(seq2[i - 1])
            i -= 1
            j -= 1
        elif direction_matrix[i][j] == 1:  # Up (deletion)
            aligned_seq1.append('-')
            aligned_seq2.append(seq2[i - 1])
            i -= 1
        else:  # Left (insertion)
            aligned_seq1.append(seq1[j - 1])
            aligned_seq2.append('-')
            j -= 1

    # Final sequences in correct order
    aligned_seq1.reverse()
    aligned_seq2.reverse()

    return ''.join(aligned_seq1), ''.join(aligned_seq2)


def hamming_distance(s1, s2, n):
    counter = 0
    for i in range(n):
        if s1[i] != s2[i]:
            counter += 1
    return counter


with open('test.txt') as f:
    strings = []
    seq = ''
    lines = f.readlines()
    for line in lines:
        if line.startswith('>'):
            if seq:
                strings.append(seq)
                seq = ''
        else:
            seq += line.strip()

    if seq:
        strings.append(seq)

s1, s2 = strings[0], strings[1]
x1, x2 = pairwise_align(s1, s2)
print(hamming_distance(x1, x2, len(x1)))
