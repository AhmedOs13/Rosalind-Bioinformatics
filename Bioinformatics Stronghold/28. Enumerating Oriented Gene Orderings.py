from itertools import permutations


def generate_permutations(elements, length):
    return list(permutations(elements, length))


n = int(input('>> n='))

test_list = []
for i in range(1, n + 1):
    test_list.append(i)
    test_list.append(-i)

generated = generate_permutations(test_list, n)
result = []

for perm in generated:
    is_true = True
    for i in range(n-1):
        for j in range(i+1,n):
            if abs(perm[i]) == abs(perm[j]):
                is_true = False
                break
    if is_true:
        result.append(perm)

print(len(result))
for perm in result:
    print(*perm)
