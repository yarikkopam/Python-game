def minmax(x, y):
    if x < y:
        return x, y
    return y, x

a = int(input())
b = int(input())
c = int(input())
d = int(input())
low1, high1 = minmax(a, b)
low2, high2 = minmax(c, d)
minimum, _ = minmax(low1, low2)
_, maximum = minmax(high1, high2)
print(minimum)
print(maximum)
