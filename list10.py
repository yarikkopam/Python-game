n = int(input())
strings = []
for i in range(n):
    strings.append(input())
longest = strings[0]
shortest = strings[0]
for s in strings:
    if len(s) > len(longest):
        longest = s
    if len(s) < len(shortest):
        shortest = s
print(longest)
print(len(longest))
print(shortest)
print(len(shortest))
