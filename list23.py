n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.sort(key=abs, reverse=True)
print(a)
