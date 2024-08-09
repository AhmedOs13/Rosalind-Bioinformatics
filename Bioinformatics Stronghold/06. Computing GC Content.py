sequences = {}
current_id = None
current_sequence = []

print("Enter your sequences. Type 'END' when you are done:")

while True:
    line = input()
    if line == "END" or line == '':
        if current_id:
            sequences[current_id] = ''.join(current_sequence)
        break
    elif line.startswith('>'):
        if current_id:
            sequences[current_id] = ''.join(current_sequence)
        current_id = line[1:]
        current_sequence = []
    else:
        current_sequence.append(line)


max_id = ''
max_cg_percentage = 0

for seq_id, sequence in sequences.items():
    count_cg = sequence.count('C') + sequence.count('G')
    cg_percentage = (count_cg / len(sequence)) * 100
    if cg_percentage > max_cg_percentage:
        max_cg_percentage = cg_percentage
        max_id = seq_id

print(f'{max_id}')
print(f'{max_cg_percentage:.6f}')
