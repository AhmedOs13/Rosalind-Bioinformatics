def count_mutations(seq_a, seq_b):
    total_mutations = 0
    length = min(len(seq_a), len(seq_b))
    for i in range(length):
        if seq_a[i] != seq_b[i]:
            total_mutations += 1
        else:
            pass

    return total_mutations


s_seq = input()
t_seq = input()
print(count_mutations(s_seq, t_seq))
