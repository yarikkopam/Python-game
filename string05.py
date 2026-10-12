n = int(input())
print("".join(chr(ord("z") - i) for i in range(n)))
