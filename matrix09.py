m = int(input())
n = int(input())
a = []
for i in range(m):
    row = [int(x) for x in input().split()]
    a.append(row)
for row in a[1::2]:
    print(row)
