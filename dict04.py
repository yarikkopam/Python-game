n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
k = input()
v = int(input())
if k in d:
    d[k] = d[k] + v
else:
    d[k] = v
print(d[k])
