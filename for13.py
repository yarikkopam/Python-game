n = int(input())
total = 0.0
sign = 1
for i in range(1, n + 1):
    total += sign * (1 + i / 10)
    sign = -sign
print(total)
