def get_reverse_array(s):
    reverse_arrays = []
    reversals = []
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            r_list = s[i:j + 1]
            r_list.reverse()
            reverse_arrays.append(s[:i] + r_list + s[j + 1:])
            reversals.append((i + 1, j + 1))
    return reverse_arrays, reversals


def get_reversal_distance(s1, s2, distance, s1_s2, s2_s1, meet_reversals):
    if s1 & s2:
        meet_reversals = list(s1 & s2)
        return s1_s2, s2_s1, meet_reversals, distance

    new_s1 = set()
    new_s1_s2 = {}
    for s in s1:
        reverse_arrays, reversals = get_reverse_array(list(s))
        for i, arr in enumerate(reverse_arrays):
            arr_tuple = tuple(arr)
            reversal = reversals[i]
            new_s1_s2[arr_tuple] = s1_s2[s] + [reversal]
            new_s1.add(arr_tuple)

    new_s2 = set()
    new_s2_s1 = {}
    for s in s2:
        reverse_arrays, reversals = get_reverse_array(list(s))
        for i, arr in enumerate(reverse_arrays):
            arr_tuple = tuple(arr)
            reversal = reversals[i]
            new_s2_s1[arr_tuple] = s2_s1[s] + [reversal]
            new_s2.add(arr_tuple)

    distance += 2

    if s1 & new_s2:
        meet_reversals = list(s1 & new_s2)
        return s1_s2, new_s2_s1, meet_reversals, distance - 1

    if s2 & new_s1:
        meet_reversals = list(s2 & new_s1)
        return new_s1_s2, s2_s1, meet_reversals, distance - 1

    if new_s1 & new_s2:
        meet_reversals = list(new_s1 & new_s2)
        return new_s1_s2, new_s2_s1, meet_reversals, distance

    return get_reversal_distance(new_s1, new_s2, distance, new_s1_s2, new_s2_s1, meet_reversals)

if __name__ == "__main__":
    with open("permutations.txt", "r") as f:
        lines = [line.strip().split(" ") for line in f.readlines() if line.strip()]

    a = [int(l) for l in lines[0]]
    b = [int(l) for l in lines[1]]

    distance = 0
    s1, s2 = set(), set()
    s1.add(tuple(a))
    s2.add(tuple(b))

    s1_s2_reversals_path, s2_s1_reversals_path, meet_reversal, distance = get_reversal_distance(
        s1, s2, distance, {tuple(a): []}, {tuple(b): []}, []
    )

    print(f"Reversal Distance: {distance}")
    result = s1_s2_reversals_path[meet_reversal[0]] + s2_s1_reversals_path[meet_reversal[0]][::-1]
    print(result)

