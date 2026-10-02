import math

def triangle_ps(a):
    perimeter = 3 * a
    area = a ** 2 * math.sqrt(3) / 4
    return perimeter, area

for i in range(3):
    a = float(input())
    p, s = triangle_ps(a)
    print(p)
    print(s)
