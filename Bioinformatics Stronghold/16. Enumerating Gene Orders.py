n = int(input('>> n='))

def permutations(elements):
    if len(elements) <= 1:
        yield elements
        return
    for perm in permutations(elements[1:]):
        for i in range(len(elements)):
            yield perm[:i] + elements[0:1] + perm[i:]

test_list = []
for i in range(n):
    test_list.append(i+1)

perm_result = list(permutations(test_list))

# Final result
print(len(perm_result))
for perm in perm_result:
    print(*perm)
