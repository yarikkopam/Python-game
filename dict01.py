n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
print(len(d))
for key in d:
    print(key)
