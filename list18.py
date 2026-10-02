n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.sort(reverse=True)
print(a)
print(len(a))
