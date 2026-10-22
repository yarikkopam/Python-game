m = int(input())
n = int(input())
values = [int(x) for x in input().split()]
a = []
for i in range(m):
    a.append(values[:])
for row in a:
    print(row)
