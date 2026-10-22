m = int(input())
n = int(input())
q = int(input())
values = [int(x) for x in input().split()]
a = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(values[j] * (q ** i))
    a.append(row)
for row in a:
    print(row)
