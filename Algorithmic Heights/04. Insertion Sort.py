def insertion_sort(array: list):
    flag = True
    counter = 0
    while flag:
        flag = False
        for i in range(0, len(array) - 1):
            if array[i] > array[i + 1]:
                flag = True
                array[i], array[i + 1] = array[i + 1], array[i]
                counter += 1
                break

    return counter


with open('test.txt') as f:
    lines = f.readlines()
    n = int(lines[0].strip())
    array = list(map(int, lines[1].strip().split()))
    print(insertion_sort(array))
