def reverse_complement(s):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in s[::-1])


def revPalindrome(dna):
    n = len(dna)
    pos_list = []
    for i in range(n):
        position = 0
        length = 0
        for j in range(4, 13):
            if i + j > n:
                break

            revComp = reverse_complement(dna[i:i + j])
            if revComp == dna[i:i + j]:
                position = i + 1
                length = j
            else:
                pass
        if position != 0:
            pos_list.append((position, length))

    return pos_list

file_path = input('>> Enter file path: ')
with open(file_path) as file:
    lines = file.readlines()
    dna = ''
    for line in lines:
        if line[0] == '>':
            pass
        else:
            dna += line.strip()

result = revPalindrome(dna)
for pal in result:
    print(pal[0], pal[1])
