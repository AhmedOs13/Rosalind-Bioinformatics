# You can see more explaination here: https://www.programiz.com/dsa/longest-common-subsequence

def lcs_algo(S1, S2, m, n):
    L = [[0 for x in range(n + 1)] for x in range(m + 1)]

    # Building the mtrix in bottom-up way
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif S1[i - 1] == S2[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    index = L[m][n]

    lcs_algo = [""] * (index + 1)
    lcs_algo[index] = ""

    i = m
    j = n
    while i > 0 and j > 0:

        if S1[i - 1] == S2[j - 1]:
            lcs_algo[index - 1] = S1[i - 1]
            i -= 1
            j -= 1
            index -= 1

        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Printing the sub sequences
    lcs = "".join(lcs_algo)
    return lcs



file_path = 'test.txt'
with open(file_path) as txt:
    lines = txt.readlines()
    dna = []
    string = ''
    for line in lines:
        if line.startswith('>'):
            if string:
                dna.append(string)
                string = ''
        else:
            string += line.strip()

    if string:
        dna.append(string)


lcs = lcs_algo(dna[0], dna[1], len(dna[0]), len(dna[1]))
print(lcs)

