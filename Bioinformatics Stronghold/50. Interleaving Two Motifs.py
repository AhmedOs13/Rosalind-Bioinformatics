def ShortestSuperSeq(m, n, x, y):
    dp = [[0 for i in range(n + 1)]
          for j in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):

            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif x[i - 1] == y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],
                                   dp[i][j - 1])
    for line in dp:
        print(*line)

    string = ""
    i = m
    j = n
    while i * j > 0:
        if x[i - 1] == y[j - 1]:
            string = x[i - 1] + string
            i -= 1
            j -= 1

        elif dp[i - 1][j] > dp[i][j - 1]:
            string = y[j - 1] + string
            j -= 1

        else:
            string = x[i - 1] + string
            i -= 1

    while i > 0:
        string = x[i - 1] + string
        i -= 1

    while j > 0:
        string = y[j - 1] + string
        j -= 1

    return string


with open('test.txt') as f:
    lines = f.readlines()
    seq_1 = lines[0].strip()
    seq_2 = lines[1].strip()
    m = len(seq_1)
    n = len(seq_2)

    if m > n:
        seq_1, seq_2 = seq_2, seq_1
        m, n = n, m
    answer = ShortestSuperSeq(m, n, seq_1, seq_2)
    print(answer)
