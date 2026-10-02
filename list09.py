n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
total = 0
for x in a:
    total += x
average = total / len(a)
big = []
for x in a:
    if x > average:
        big.append(x)
print(big)
print(len(big))
