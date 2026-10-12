n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
v = int(input())
for key in list(d):
    if d[key] < v:
        del d[key]
print(len(d))
