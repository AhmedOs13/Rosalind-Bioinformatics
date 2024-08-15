'''
E: Number of Edges
N: Number of Nodes
L: Number of Leaves
I: Number of Internal Nodes


We know that E = N - 1
AND N = L + I
SO E = L + I - 1

We know that in unrooted tree
we have 3 Internal node AND 1 Leaf in each edge

Total degree sum = 3I + L

ALSO Total degree sum = 2E
SO,
2L + 2I - 2 = 3I + L
I = L - 2
'''

L = input('>> ')
I = L - 2
print(I)
