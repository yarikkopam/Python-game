def digit_count(k):
    count = 0
    while k > 0:
        count += 1
        k //= 10
    return count

for i in range(5):
    k = int(input())
    print(digit_count(k))
