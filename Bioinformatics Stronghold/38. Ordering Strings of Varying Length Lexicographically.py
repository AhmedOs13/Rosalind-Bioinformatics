def variation(alpha, place):
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

    permutations = set(permutations)

    return permutations


def custom_sort(string, alpha):
    order = {char: idx for idx, char in enumerate(alpha)}
    sorted_strings = sorted(string, key=lambda x: [order.get(c) for c in x])
    return sorted_strings


alpha = list(input().split())
place = int(input())
permutations = []
for i in range(1, place + 1):
    result = variation(alpha, i)
    permutations.extend(result)

final = custom_sort(permutations, alpha)

for perm in final:
    print(perm)
