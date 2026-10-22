m = int(input())
n = int(input())
a = []
for i in range(m):
    row = []
    for j in range(1, n + 1):
        row.append(5 * j)
    a.append(row)
for row in a:
    print(row)
