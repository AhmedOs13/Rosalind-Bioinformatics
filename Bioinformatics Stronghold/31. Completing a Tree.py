file_path = 'test.txt'
with open(file_path) as txt:
    array = []
    lines = txt.readlines()
    n = int(lines[0].strip())
    for line in lines[1:]:
        a, b = map(int, line.strip().split())
        array.append([a, b])

# Let's Construct the TREE!
tree = []
numbers = []
for pair in array:
    found = False
    for branch in tree:
        if pair[0] in branch:
            found = True
            branch.append(pair[1])
            break
        elif pair[1] in branch:
            found = True
            branch.append(pair[0])
            break
    if pair[0] not in numbers:
        numbers.append(pair[0])
    if pair[1] not in numbers:
        numbers.append(pair[1])

    if not found:
        tree.append(pair)

# Check if there are a connection between leafs
not_com = True
while not_com:
    not_com = False
    for leaf1 in tree:
        for i in leaf1:
            for leaf2 in tree:
                if leaf1 != leaf2:
                    if i in leaf2:
                        leaf1.extend(leaf2)
                        tree.remove(leaf2)
                        not_com = True
                        break
            if not_com:
                break
        if not_com:
            break

# Add missed numbers as an individual leaf
for i in range(1,n+1):
    if i not in numbers:
        tree.append([i])

# Edges required is k-1
print(len(tree)-1)
