n = int(input())
d1 = {}
for i in range(n):
    key = input()
    value = int(input())
    d1[key] = value
m = int(input())
ignored = 0
for i in range(m):
    key = input()
    value = int(input())
    if key in d1:
        ignored += 1
    else:
        d1[key] = value
print(len(d1))
print(ignored)
