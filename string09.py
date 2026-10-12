n = int(input())
c1 = input()
c2 = input()
print("".join(c1 if i % 2 == 0 else c2 for i in range(n)))
