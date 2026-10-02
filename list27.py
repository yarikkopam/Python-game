n = int(input())
rows = []
for i in range(n):
    x = float(input())
    y = float(input())
    rows.append([x, y])
rows.sort(key=lambda r: r[0], reverse=True)
for r in rows:
    print(r)
print(rows[0])
