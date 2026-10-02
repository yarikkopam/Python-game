n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
d = int(input())
print(a.count(d))
if d in a:
    print(a.index(d))
else:
    print(-1)
