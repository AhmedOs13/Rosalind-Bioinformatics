AA_AA, AA_Aa, AA_aa, Aa_Aa, Aa_aa, aa_aa = map(int, input('>> ').split())

result = 0
result += AA_AA * 2  # 100%
result += AA_Aa * 2  # 100%
result += AA_aa * 2  # 100%
result += Aa_Aa * 1.5  # 75%
result += Aa_aa * 1  # 50%
# aa_aa has 0% probability

print(result)
