def power_a234(a):
    return a ** 2, a ** 3, a ** 4

for i in range(5):
    a = float(input())
    a2, a3, a4 = power_a234(a)
    print(a2)
    print(a3)
    print(a4)
