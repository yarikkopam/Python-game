n = int(input())
strings = []
for i in range(n):
    strings.append(input())
letter = input()
starts = [s for s in strings if s[0] == letter]
print(starts)
