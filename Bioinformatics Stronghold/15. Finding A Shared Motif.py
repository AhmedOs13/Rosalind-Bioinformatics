# Opening TEST file
file_path = input("Enter the file path:")
strings = []
dna_string = ''
with open(file_path) as fasta:
    lines = fasta.readlines()
    for line in lines:
        line = line.strip()
        if line[0] == '>':
            if dna_string != '':
                strings.append(dna_string)
                dna_string = ''
            pass
        else:
            dna_string += line
if dna_string != '':
    strings.append(dna_string)

# Saving all possible substring in one list
first_sub = []
for i in range(len(strings[0])):
    for j in range(i,len(strings[0])+1):
        sub = ''
        sub = strings[0][i:j]
        if sub != '':
            first_sub.append(sub)

# Sorting subs descinding by length
first_sub.sort(key=len,reverse=True)

# Iterating to find the longest common substring
for sub in first_sub:
    is_sub = True
    for string in strings:
        if sub in string:
            pass
        else:
            is_sub = False
            break
    if is_sub:
        common_sub = sub
        break

# Final result
print(common_sub)
