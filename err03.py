try:
    a = int(input())
    b = int(input())
    print(a / b)
except ValueError:
    print("Ошибка ввода")
except ZeroDivisionError:
    print("Делить на ноль нельзя")
