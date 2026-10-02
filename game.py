# ================================================
# ИГРА «ЗАБЫТЫЙ РУДНИК»
# Автор: Александров Ярослав
# Дата: октябрь 2026
#
# Пункт 4 — «постучать по стене»: герой простукивает
# породу и слушает эхо. Бесплатное действие: стоять
# и слушать ничего не стоит.
#
# Пункт 6 — «тренировка»: герой наносит серию ударов
# по тренировочной глыбе, каждый третий удар — критический.
# ================================================

# --- Заголовок ------------------------------------
title = "ЗАБЫТЫЙ РУДНИК"
frame = "=" * 20

print(frame)
print("   " + title + "   ")
print(frame)
print()

# --- Знакомство с героем --------------------------
print("Как зовут героя?")
hero_name = input()
print(f"Добро пожаловать, {hero_name}!")
print("Ты входишь в старый рудник. Здесь темно, пахнет пылью и железом.")
print()

# --- Настройка героя ------------------------------
print("Настройка героя.")
print("Здоровье, сила, ловкость, удача — по одному числу в строке:")
health = int(input())
strength = int(input())
agility = int(input())
luck = int(input())

# --- Расчёт урона ---------------------------------
base_attack = 10
damage = base_attack + strength * 1.5
crit_damage = damage * 2
stamina = health // 10 + luck

# --- Формуляр героя -------------------------------
print("Характеристики героя:")
print(f"Здоровье:   {health}")
print(f"Сила:       {strength}")
print(f"Ловкость:   {agility}")
print(f"Удача:      {luck}")
print()
print(f"Урон героя: {damage:.1f}")
print(f"Критический урон: {crit_damage:.1f}")
print(f"Запас сил: {stamina}")
print()

# --- Главный цикл игры ----------------------------
running = True
actions = 0
while running:
    print("Что делаешь?")
    print("1 - осмотреться")
    print("2 - идти вперёд")
    print("3 - отдохнуть")
    print("4 - постучать по стене")
    print("5 - зажечь фонарь")
    print("6 - тренировка")
    print("0 - выйти из рудника")
    valid = ("0", "1", "2", "3", "4", "5", "6")
    choice = input()
    while choice not in valid:
        print("Такого пункта нет. Введи номер пункта из меню.")
        choice = input()
    match choice:
        case "1":
            print("Ты осматриваешься. В стенах старые следы кирки, на полу пыль.")
        case "2":
            cost = 2
            if stamina >= cost:
                stamina -= cost
                print("Ты осторожно идёшь вперёд. Гравий хрустит под ногами.")
            else:
                health -= cost - stamina
                stamina = 0
                print("Сил больше нет — ты идёшь на одном упорстве.")
        case "3":
            stamina += 3
            print("Ты садишься на груду досок и переводишь дух. Силы возвращаются.")
        case "4":
            print("Ты стучишь по стене. Где-то в глубине эхо отвечает глухим раскатом.")
        case "5":
            stamina -= 1
            print("Ты зажигаешь фонарь. Дрожащий свет вытягивает из темноты стены рудника.")
        case "6":
            strikes = 6
            train_cost = 4
            total_damage = 0
            crit_count = 0
            print("Ты подходишь к тренировочной глыбе.")
            print("Её оставил здесь прошлый рудокоп — для разминки перед спуском.")
            print()
            print(f"Наносите {strikes} ударов.")
            for i in range(1, strikes + 1):
                hit_damage = damage
                if i % 3 == 0:
                    hit_damage = crit_damage
                if hit_damage == crit_damage:
                    print(f"Удар {i}: {hit_damage:.1f} — критический!")
                    crit_count += 1
                else:
                    print(f"Удар {i}: {hit_damage:.1f}")
                total_damage += hit_damage
            print()
            print(f"Итог: {strikes} ударов, критических: {crit_count}.")
            print(f"Общий урон: {total_damage:.1f}")
            print(f"Средний урон: {total_damage / strikes:.1f}")
            stamina -= train_cost
        case "0":
            print("Ты поднимаешься по лестнице к свету. Рудник остаётся позади.")
            running = False
    if running:
        actions += 1
    print()
    print(f"Здоровье: {health}  Запас сил: {stamina}")
    if health <= 0:
        print(f"{hero_name} падает без сил. Рудник забирает ещё одного искателя.")
        running = False

# --- Прощание -------------------------------------
print(frame)
if health <= 0:
    print(f"Ты не дошёл, {hero_name}. Действий совершено: {actions}.")
else:
    print(f"Забег окончен, {hero_name}. Действий совершено: {actions}.")
print(frame)
