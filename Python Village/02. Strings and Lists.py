string = input()
x1, y1, x2, y2 = map(int, input().split())

print(string[x1:x2 + 1], string[y1:y2 + 1])
