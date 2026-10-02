n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
total = 0
for i in range(1, len(a), 2):
    print(a[i])
    total += a[i]
print(total)
