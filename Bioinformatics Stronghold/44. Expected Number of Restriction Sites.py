def probability(s, n, m, A):
    AT = s.count('T') + s.count('A')
    CG = s.count('C') + s.count('G')

    B = []
    for gc_content in A:
        prob_CG = (gc_content / 2) ** CG
        prob_AT = ((1 - gc_content) / 2) ** AT
        comb = n - m + 1
        error = 0.0001  # To handle the 0.5 rounding
        total_prop = (prob_CG * prob_AT * comb)

        B.append(round(total_prop, 3))

    return B


n = int(input())
s = input()
A = list(map(float, input().split()))

m = len(s)

B = probability(s, n, m, A)
print(*B)
