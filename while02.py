a = int(input())
b = int(input())
free = a
count = 0
while free >= b:
    free -= b
    count += 1
print(count)
