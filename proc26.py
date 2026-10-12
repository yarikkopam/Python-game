def is_power5(k):
    if k <= 0:
        return False
    while k % 5 == 0:
        k //= 5
    return k == 1

count = 0
for i in range(10):
    k = int(input())
    if is_power5(k):
        count += 1
print(count)
