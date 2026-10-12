def digit_n(k, n):
    pos = 1
    cur = k
    while cur > 0:
        if pos == n:
            return cur % 10
        cur //= 10
        pos += 1
    return -1

for i in range(5):
    k = int(input())
    for n in range(1, 6):
        print(digit_n(k, n))
