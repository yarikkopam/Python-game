a = float(input())
total = 0.0
k = 0
while total + 1 / (k + 1) < a:
    k += 1
    total += 1 / k
print(k)
print(total)
