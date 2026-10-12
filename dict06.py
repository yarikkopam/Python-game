n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
total = 0
for value in d.values():
    total = total + value
print(total)
