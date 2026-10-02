n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
imax = 0
for i in range(len(a)):
    if a[i] > a[imax]:
        imax = i
print(imax)
print(a[imax])
