n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
average = sum(a) / len(a)
big = [x for x in a if x > average]
print(big)
print(average)
