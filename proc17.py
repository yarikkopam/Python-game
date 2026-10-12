def roots_count(a, b, c):
    d = b * b - 4 * a * c
    if abs(d) < 1e-9:
        return 1
    if d > 0:
        return 2
    return 0

for i in range(3):
    a = float(input())
    b = float(input())
    c = float(input())
    print(roots_count(a, b, c))
