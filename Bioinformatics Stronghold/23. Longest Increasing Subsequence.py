def longest_increasing_subsequence(sequence):
    n = len(sequence)
    lis = [[] for _ in range(n)]

    for i in range(n):
        for j in range(i):
            if sequence[j] < sequence[i] and len(lis[j]) > len(lis[i]):
                lis[i] = lis[j][:]
        lis[i].append(sequence[i])

    longest = []
    for subseq in lis:
        if len(subseq) > len(longest):
            longest = subseq

    return longest


def longest_decreasing_subsequence(sequence):
    n = len(sequence)
    lds = [[] for _ in range(n)]

    for i in range(n):
        for j in range(i):
            if sequence[j] > sequence[i] and len(lds[j]) > len(lds[i]):
                lds[i] = lds[j][:]
        lds[i].append(sequence[i])

    longest = []
    for subseq in lds:
        if len(subseq) > len(longest):
            longest = subseq

    return longest


n = int(input())
sequence = list(map(int, input().split()))

longest_asc = longest_increasing_subsequence(sequence)
longest_desc = longest_decreasing_subsequence(sequence)

print(*longest_asc)
print(*longest_desc)
