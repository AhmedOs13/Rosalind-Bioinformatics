dict_test = {}
string = list(input('>> ').split())

for word in string:
    if word in dict_test.keys():
        dict_test[word] += 1
    else:
        dict_test[word] = 1

for key, value in dict_test.items():
    print(key, value)
