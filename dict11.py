n = int(input())
counts = {}
for i in range(n):
    word = input()
    counts[word] = counts.get(word, 0) + 1
for word, count in counts.items():
    print(f"{word}: {count}")
