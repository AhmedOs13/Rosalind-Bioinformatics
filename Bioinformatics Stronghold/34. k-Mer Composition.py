def k_mers(alpha, place):
    basic = []
    for char in alpha:
        string = ''
        string += char * place
        basic.append(string)

    permutations = basic.copy()

    for i in range(place):
        new_permutations = []
        for perm in permutations:
            for char in alpha:
                tmp = perm[:i] + char + perm[i + 1:]
                if tmp not in permutations and tmp not in new_permutations:
                    new_permutations.append(tmp)
        permutations.extend(new_permutations)

    permutations = sorted(set(permutations))
    return permutations


alpha = ['A', 'C', 'G', 'T']
place = 4

mers = k_mers(alpha, place)
mers.sort()
occurance = {}

file_path = input('>> Enter file path: (Without Quotes) \n')
with open(file_path) as f:
    lines = f.readlines()
    dna = ''.join(line.strip() for line in lines[1:])

for i in range(len(dna) - 3):
    if dna[i:i+4] in occurance:
        occurance[dna[i:i + 4]] += 1
    else:
        occurance[dna[i:i+4]] = 1

for mer in mers:
    print(occurance[mer], end=' ')
