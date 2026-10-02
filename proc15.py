def shift_left3(a, b, c):
    return b, c, a

for i in range(2):
    a = float(input())
    b = float(input())
    c = float(input())
    print(shift_left3(a, b, c))
