n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
d = int(input())
multiplied = [x * d for x in a]
print(multiplied)
print(a.count(d))
