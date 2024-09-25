def binary_search(array, value, low, high):
    mid_index = (high + low) // 2
    if low > high:
        return -1

    if array[mid_index] == value:
        return mid_index + 1
    elif array[mid_index] > value:
        return binary_search(array, value, low, mid_index - 1)
    elif array[mid_index] < value:
        return binary_search(array, value, mid_index + 1, high)


with open('test.txt') as f:
    lines = f.readlines()
    array = list(map(int, lines[2].strip().split()))
    values = list(map(int, lines[3].strip().split()))

for value in values:
    print(binary_search(array, value, 0, len(array) - 1), end=' ')
