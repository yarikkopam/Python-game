word = input()
index = int(input())
try:
    print(word[index])
except IndexError:
    print("Нет такого символа")
