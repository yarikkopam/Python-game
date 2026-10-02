try:
    number = int(input())
    print(number)
except ValueError as e:
    print(e)
    print(type(e))
