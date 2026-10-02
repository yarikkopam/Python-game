def swap(x, y):
    return y, x

a = float(input())
b = float(input())
c = float(input())
d = float(input())
a, b = swap(a, b)
c, d = swap(c, d)
b, c = swap(b, c)
print(a)
print(b)
print(c)
print(d)
