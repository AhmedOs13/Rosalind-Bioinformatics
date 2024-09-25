def distance_tree(T, x, y):
    x_index, y_index = T.find(x), T.find(y)
    sub_tree = [i for i in T[min(x_index, y_index):max(x_index, y_index)] if i in '(),']
    sub_tree_str = ''.join(sub_tree)
    while '(,)' in sub_tree_str:
        sub_tree_str = sub_tree_str.replace('(,)', '')

    open_count = sub_tree_str.count('(')
    close_count = sub_tree_str.count(')')
    comma_count = sub_tree_str.count(',')

    if open_count == len(sub_tree_str) or close_count == len(sub_tree_str):
        return len(sub_tree_str)
    elif comma_count == len(sub_tree_str):
        return 2
    else:
        return open_count + close_count + 2


with open('test.txt', 'r') as f:
    tree = [line.strip().replace(';', '') for line in f.readlines() if len(line.strip()) > 0]
for i in range(0, len(tree), 2):
    T = tree[i]
    x, y = tree[i + 1].split()
    print(distance_tree(T, x, y), end=" ")
