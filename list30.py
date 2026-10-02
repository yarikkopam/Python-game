n = int(input())
strings = []
for i in range(n):
    strings.append(input())
lengths = [len(s) for s in strings]
print(lengths)
print(sum(lengths))
