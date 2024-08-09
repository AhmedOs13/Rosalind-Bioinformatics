alpha = list(input().split())
place = int(input())

alpha = sorted(alpha)

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

for perm in permutations:
    print(perm)
