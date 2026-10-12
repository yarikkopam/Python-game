def is_power_n(k, n):
    if k <= 0:
        return False
    while k % n == 0:
        k //= n
    return k == 1

n = int(input())
count = 0
for i in range(10):
    k = int(input())
    if is_power_n(k, n):
        count += 1
print(count)
