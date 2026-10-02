n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
d = int(input())
if d in a:
    a.remove(d)
print(a)
print(len(a))
