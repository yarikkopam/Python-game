m = int(input())
n = int(input())
a = []
for i in range(1, m + 1):
    row = []
    for j in range(n):
        row.append(10 * i)
    a.append(row)
for row in a:
    print(row)
