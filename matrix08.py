m = int(input())
n = int(input())
a = []
for i in range(m):
    row = [int(x) for x in input().split()]
    a.append(row)
k = int(input())
print([row[k - 1] for row in a])
