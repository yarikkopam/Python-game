try:
    n = int(input())
    result = 100 / n
except ValueError:
    print("Ошибка ввода")
except ZeroDivisionError:
    print("Делить на ноль нельзя")
else:
    print(result)
finally:
    print("Вычисление завершено")
