a = int(input())
b = int(input())
try:
    print(f"{a / b:.1f}")
except ZeroDivisionError:
    print("Делить на ноль нельзя")
