import re
import requests


def get_sequence(protein_code):
    protein_code = protein_code.split('_')[0]
    url = f'https://rest.uniprot.org/uniprotkb/{protein_code}.fasta'
    response = requests.get(url)

    if response.status_code == 200:
        fasta_data = response.text.splitlines()
        sequence = ''.join(fasta_data[1:]).strip()
        return sequence
    else:
        print(f"Failed to retrieve data for {protein_code}: {response.status_code}")
        return None


def find_motif_locations(sequence):
    pattern = r'(?=N[^P][ST][^P])'
    prog = re.compile(pattern)
    matches = [match.start() + 1 for match in prog.finditer(sequence)]
    return matches

file_path = input('>> Enter your file path: (Without quotes) \n')
with open(file_path) as test_file:
    result = {}
    for line in test_file:
        uniprot_id = line.strip()
        sequence = get_sequence(uniprot_id)
        if sequence:
            locations = find_motif_locations(sequence)
            if locations:
                result[uniprot_id] = locations

for key, value in result.items():
    if value:
        print(key)
        print(*value)
