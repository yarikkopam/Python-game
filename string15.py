s = input()
lat = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
rus = "абвгдежзийклмнопрстуфхцчшщъыьэюяёАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯЁ"
alphabet = lat + rus
count = 0
for ch in s:
    if ch in alphabet and ch.islower():
        count += 1
print(count)
