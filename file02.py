name = input()
n = int(input())
with open(name, "w", encoding="utf-8") as f:
    for i in range(1, n + 1):
        f.write(str(2 * i) + "\n")
