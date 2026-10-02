n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
sq = [x * x for x in a]
print(sq)
print(sum(sq))
