n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
k = input()
if k in d:
    print(d[k])
else:
    print("нет такого ключа")
