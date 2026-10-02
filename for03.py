a = int(input())
b = int(input())
count = 0
for i in range(b - 1, a, -1):
    print(i)
    count += 1
print(count)
