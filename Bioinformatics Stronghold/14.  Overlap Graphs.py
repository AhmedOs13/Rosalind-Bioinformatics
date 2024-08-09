motif = {}
file_path = input("Enter the path of the file: ")
with open(file_path) as test:
    lines = test.readlines()
    dna_string = ''
    key = ''
    for i in range(len(lines)):
        s = lines[i].strip()
        if s.startswith('>'):
            if key != '':
                motif[key] = dna_string
            key = s[1:]
            dna_string = ''
        else:
            dna_string += s
    if key != '':
        motif[key] = dna_string

for key_1, dna_1 in motif.items():
    for key_2, dna_2 in motif.items():
        if key_1 != key_2 and dna_1[-3:] == dna_2[:3]:
            print(key_1, key_2)
