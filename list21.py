n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
positive = [x for x in a if x > 0]
print(positive)
print(len(positive))
