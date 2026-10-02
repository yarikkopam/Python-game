while True:
    try:
        choice = int(input())
    except ValueError:
        print("Введите число")
        continue
    if 1 <= choice <= 5:
        break
    print("Такого пункта нет")
print(choice)
