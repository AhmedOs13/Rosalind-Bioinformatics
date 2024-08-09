file_path = input('Enter your file path: ')
message = []
with open(file_path) as file:
    lines = file.readlines()
    for line in lines:
        message.append(line)

data = message[1::2]
answer = ''.join(data)

with open("output.txt", "w") as file:
    file.write(answer)

print('Your file saved: output.txt')
