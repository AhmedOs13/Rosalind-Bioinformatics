# Using Bio Library
from Bio.Seq import Seq
dna = Seq("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")
print(dna.count('A'),dna.count('C'),dna.count('G'),dna.count('T'))

# 0.3165 s, Memory: 1555.12 kB

# -----------------------------------------------------------------------------------

# Using GeneMaster Library
from GeneMaster import DNA
dna = DNA("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")
print(dna.A, dna.C, dna.G, dna.T)

# Time: 0.0288 s, Memory: 129.85 kB
