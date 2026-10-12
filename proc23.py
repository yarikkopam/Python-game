def quarter(x, y):
    if x > 0 and y > 0:
        return 1
    if x < 0 and y > 0:
        return 2
    if x < 0 and y < 0:
        return 3
    return 4

for i in range(3):
    x = float(input())
    y = float(input())
    print(quarter(x, y))
