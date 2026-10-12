n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
rev = {}
for key, value in d.items():
    rev[value] = key
for value, key in rev.items():
    print(f"{value}: {key}")
