def circle_s(r):
    return 3.14 * r * r

def ring_s(r1, r2):
    return circle_s(r1) - circle_s(r2)

for i in range(3):
    r1 = float(input())
    r2 = float(input())
    print(ring_s(r1, r2))
