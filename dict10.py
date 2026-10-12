n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
for name, price in d.items():
    print(f"{name}: {price}")
