def build_trie(seqs):
    current_node = 2
    node_map = {}
    edges = []

    for seq in seqs:
        parent_node = 1
        for c in seq:
            if (parent_node, c) not in node_map:
                node_map[(parent_node, c)] = current_node
                edges.append((parent_node, current_node, c))
                parent_node = current_node
                current_node += 1
            else:
                parent_node = node_map[(parent_node, c)]

    return edges


with open('test.txt') as f:
    seqs = [line.strip() for line in f.readlines()]

edges = build_trie(seqs)

for parent, child, symbol in edges:
    print(parent, child, symbol)
