def sign(x):
    if x < 0:
        return -1
    if x == 0:
        return 0
    return 1

a = float(input())
b = float(input())
print(sign(a) + sign(b))
