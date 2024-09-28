with open('test.txt') as f:
    lines = f.readlines()
    s1 = set(map(float, lines[0].strip().split()))
    s2 = set(map(float, lines[1].strip().split()))

diff = dict()
for a in s1:
    for b in s2:
        diff_ab = round(abs(a-b),5)
        if diff_ab not in diff:
            diff[diff_ab] = 1
        else:
            diff[diff_ab] += 1

diff = list(sorted(diff.items(), key=lambda item: item[1], reverse=True))[0]
print(f'{diff[1]}\n{diff[0]}')
