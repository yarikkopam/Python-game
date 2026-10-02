def invert_digits(k):
    rev = 0
    while k > 0:
        rev = rev * 10 + k % 10
        k //= 10
    return rev

for i in range(5):
    k = int(input())
    print(invert_digits(k))
