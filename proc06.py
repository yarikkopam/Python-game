def digit_count_sum(k):
    count = 0
    total = 0
    while k > 0:
        total += k % 10
        count += 1
        k //= 10
    return count, total

for i in range(5):
    k = int(input())
    c, s = digit_count_sum(k)
    print(c)
    print(s)
