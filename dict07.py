n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
best = None
for key in d:
    if best is None or d[key] > d[best]:
        best = key
print(best)
