n = int(input())
rest = n
while rest % 3 == 0:
    rest //= 3
print(rest == 1)
