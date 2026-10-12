def sum_range(a, b):
    if a > b:
        return 0
    total = 0
    for k in range(a, b + 1):
        total += k
    return total

a = int(input())
b = int(input())
c = int(input())
print(sum_range(a, b))
print(sum_range(b, c))
