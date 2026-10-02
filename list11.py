n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k = 0
for i in range(len(a)):
    if a[i] < 0:
        a[i] = 0
        k = k + 1
print(a)
print(k)
