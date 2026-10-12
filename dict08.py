n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
v = int(input())
print(v in d.values())
