with open('test.txt') as f:
    lines = f.readlines()
    n = int(lines[0].strip())
    A = set(map(int,lines[1][1:-2].split(', ')))
    B = set(map(int,lines[2][1:-2].split(', ')))


all_set = set(i+1 for i in range(n))
union = A.union(B)                     # A | B
intersection = A.intersection(B)       # A & B
A_B = A.difference(B)                  # A - B
B_A = B.difference(A)                  # B - A
A_c = all_set.difference(A)            # all_set - A
B_c = all_set.difference(B)            # all_set - B

print(union)
print(intersection)
print(A_B)
print(B_A)
print(A_c)
print(B_c)
