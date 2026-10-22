name = input()
try:
    with open(name, "w", encoding="utf-8"):
        pass
    print(True)
except OSError:
    print(False)
