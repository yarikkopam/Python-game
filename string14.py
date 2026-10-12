s = input()
count = 0
for ch in s:
    if ch.isupper() and "A" <= ch <= "Z":
        count += 1
print(count)
