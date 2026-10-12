def even(k):
    return k % 2 == 0

count = 0
for i in range(10):
    k = int(input())
    if even(k):
        count += 1
print(count)
