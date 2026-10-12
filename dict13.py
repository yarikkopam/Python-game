n = int(input())
d = {}
for i in range(n):
    name = input()
    price = int(input())
    qty = int(input())
    d[name] = [price, qty]
total = 0
best = None
best_cost = -1
for name in d:
    price, qty = d[name]
    cost = price * qty
    total += cost
    if cost > best_cost:
        best_cost = cost
        best = name
print(total)
print(best)
