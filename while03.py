n = int(input())
k = int(input())
quotient = 0
rest = n
while rest >= k:
    rest -= k
    quotient += 1
print(quotient)
print(rest)
