word = input()
try:
    index = int(input())
    print(word[index])
except ValueError:
    print("Ошибка ввода")
except IndexError:
    print("Нет такого символа")
