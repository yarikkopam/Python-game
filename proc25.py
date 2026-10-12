def is_square(k):
    if k <= 0:
        return False
    r = int(k ** 0.5)
    return r * r == k or (r + 1) * (r + 1) == k

count = 0
for i in range(10):
    k = int(input())
    if is_square(k):
        count += 1
print(count)
