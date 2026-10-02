def sort_inc3(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return a, b, c

for i in range(2):
    a = float(input())
    b = float(input())
    c = float(input())
    print(sort_inc3(a, b, c))
