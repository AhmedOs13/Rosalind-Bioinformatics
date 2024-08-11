from math import log10

def count_AT_GC(dna):
    AT = dna.count('A') + dna.count('T')
    GC = dna.count('G') + dna.count('C')

    return AT, GC


def probabilities(dna, A):
    B = []
    AT, GC = count_AT_GC(dna)
    for prob in A:
        x = prob / 2
        y = (1 - prob) / 2

        GC_res = x ** GC
        GC_log = log10(GC_res)
        AT_res = y ** AT
        AT_log = log10(AT_res)

        result_log = GC_log + AT_log
        B.append(round(result_log, 3))

    return B

dna = input()
A = list(map(float,input().split()))

probability = probabilities(dna, A)
print(*probability)



