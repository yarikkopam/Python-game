def rect_ps(x1, y1, x2, y2):
    side_a = abs(x2 - x1)
    side_b = abs(y2 - y1)
    perimeter = 2 * (side_a + side_b)
    area = side_a * side_b
    return perimeter, area

for i in range(3):
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    p, s = rect_ps(x1, y1, x2, y2)
    print(p)
    print(s)
