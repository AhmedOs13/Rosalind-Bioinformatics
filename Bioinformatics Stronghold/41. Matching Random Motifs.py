def matching_probability(N, x, s):
    p_s = 1.0
    for char in s:
        if char in 'CG':
            p_s *= x / 2
        else:
            p_s *= (1 - x) / 2

    at_least_one_match = 1 - (1 - p_s) ** N
    return at_least_one_match


N, x = map(float, input().split())
s = input()

result = matching_probability(N, x, s)

print(f'{result:.3f}')
