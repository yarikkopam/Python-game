name = input()
a = float(input())
d = float(input())
with open(name, "w", encoding="utf-8") as f:
    for i in range(10):
        f.write(str(a + i * d) + "\n")
