n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k = int(input())
a.sort(reverse=True)
print(a[:k])
