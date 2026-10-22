m = int(input())
n = int(input())
a = []
for i in range(m):
    row = [int(x) for x in input().split()]
    a.append(row)
for j in range(0, n, 2):
    for i in range(m):
        print(a[i][j])
