from math import factorial


def perfect_match(rna):
    count_A = rna.count('A')
    count_C = rna.count('C')
    combinations = factorial(count_A) * factorial(count_C)
    return combinations


file_path = input('>> ')
with open(file_path) as file:
    lines = file.readlines()
    rna = ''
    for line in lines:
        if line[0] != '>':
            rna += line.strip()

result = perfect_match(rna)
print(result)
