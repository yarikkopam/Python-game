n = int(input())
strings = []
for i in range(n):
    strings.append(input())
print(sorted(strings, key=len))
print(max(strings, key=len))
