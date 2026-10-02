n = int(input())
total = 0
k = 0
while total + k + 1 <= n:
    k += 1
    total += k
print(k)
print(total)
