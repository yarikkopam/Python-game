n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k1 = int(input())
k2 = int(input())
b = a[k1:k2 + 1]
print(b)
s = 0
for x in b:
    s = s + x
print(s)
