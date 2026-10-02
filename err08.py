total = 0
skipped = 0
while True:
    line = input()
    if line == "":
        break
    try:
        total += int(line)
    except ValueError:
        skipped += 1
        print("Пропущено: не число")
print(total)
print(skipped)
