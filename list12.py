n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k = int(input())
a.insert(k, 0)
print(a)
print(len(a))
