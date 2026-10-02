def add_left_digit(d, k):
    digits = 1
    rest = k
    while rest >= 10:
        rest //= 10
        digits += 1
    return d * 10 ** digits + k

k = int(input())
d1 = int(input())
d2 = int(input())
k = add_left_digit(d1, k)
print(k)
k = add_left_digit(d2, k)
print(k)
