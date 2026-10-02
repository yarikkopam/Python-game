n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
total = 0
for x in a:
    total += x
product = 1
for i in range(0, len(a), 2):
    product *= a[i]
print(total)
print(product)
