# ================================================
# ИГРА «ЗАБЫТЫЙ РУДНИК»
# Автор: Александров Ярослав
# Дата: октябрь 2026
#
# Пункт 4 — «постучать по стене»: герой простукивает
# породу и слушает эхо. Бесплатное действие.
#
# Пункт 6 — «тренировка»: серия ударов по глыбе,
# каждый третий удар — критический.
#
# Пункт 7 — «спуск вниз»: случайный враг, бой раундами,
# журнал раундов. Победа приносит золото (трофеи).
#
# Пункт 8 — «лидерборд»: топ-3 раундов по урону героя
# и рекорд врага за весь забег.
#
# Пункт 9 — «магазин»: золото тратится на зелья, масло
# и эликсир. Количество по умолчанию 1 (пустой ввод),
# надбавка урона передаётся в бой именованным bonus=.
# Эликсир даёт +2 к урону за штуку до конца забега
# (надбавка прибавляется после крита).
# ================================================

import random

# --- Правила игры ---------------------------------
title = "ЗАБЫТЫЙ РУДНИК"
frame = "=" * 20

base_attack = 10
enemy_hp_start = 45

enemies = ["гуль", "скелет", "паук", "нетопырь"]
log = []
gold_total = 0
ability_bonus = 0


# --- Функции --------------------------------------

def hero_hit(strike_n):
    """Урон героя в удар номер strike_n: каждый третий — критический.

    Берёт правила damage и crit_damage из верха файла.
    Возвращает урон удара (вещественное число).
    """
    if strike_n % 3 == 0:
        return crit_damage
    return damage


def fight(enemy, hero_health, bonus=0):
    """Бой с enemy до гибели одного из двоих.

    bonus — надбавка к урону героя, по умолчанию 0: без эликсира
    бой идёт как прежде. Надбавка прибавляется к удару после
    крита. Печатает строки раундов.
    Возвращает (rounds, won, hero_health, loot): таблица раундов,
    признак победы, здоровье после боя и трофеи (0 при поражении).
    """
    enemy_hp = enemy_hp_start
    round_n = 0
    strike_n = 0
    rounds = []
    while enemy_hp > 0 and hero_health > 0:
        strike_n += 1
        round_n += 1
        hit = hero_hit(strike_n) + bonus
        enemy_hp -= hit
        enemy_strike = 0
        mark = "."
        if hero_hit(strike_n) == crit_damage:
            mark = " — критический!"
        if enemy_hp <= 0:
            print(f"Раунд {round_n}: ты наносишь {hit:.1f} урона{mark} Враг падает.")
        else:
            enemy_strike = random.randint(2, 6)
            hero_health -= enemy_strike
            print(f"Раунд {round_n}: ты наносишь {hit:.1f} урона{mark} Здоровье врага: {enemy_hp:.1f}. Враг бьёт в ответ на {enemy_strike}.")
        rounds.append([round_n, hit, enemy_strike])
    won = enemy_hp <= 0
    if won:
        loot = 10 + 5 * round_n
    else:
        loot = 0
    return rounds, won, hero_health, loot


def buy(price, gold, quantity=1):
    """Покупает quantity штук товара ценой price за золото gold.

    quantity по умолчанию 1. Возвращает (gold_left, ok): остаток
    золота и признак успешной покупки. Ничего не печатает.
    """
    cost = price * quantity
    if gold >= cost:
        return gold - cost, True
    return gold, False


def print_leaderboard(battle_log):
    """Печатает топ-3 раундов по урону героя и рекорд врага.

    Ничего не возвращает (None): контракт — вывести.
    """
    if not battle_log:
        print("Ты ещё не дрался в этом забеге.")
        return
    top = sorted(battle_log, key=lambda r: r[1], reverse=True)[:3]
    print("Лидерборд (урон героя):")
    for i in range(len(top)):
        print(f"{i + 1}. Раунд {top[i][0]}: {top[i][1]:.1f}")
    worst = max(battle_log, key=lambda r: r[2])
    print(f"Сильнейший удар врага: {worst[2]} (раунд {worst[0]}).")


def print_run_summary(battle_log):
    """Печатает суммарный и средний урон героя за забег.

    Ничего не возвращает (None): контракт — вывести.
    """
    total = sum(r[1] for r in battle_log)
    rounds = len(battle_log)
    if rounds > 0:
        print(f"Урон: {total:.1f} за {rounds} раундов, в среднем {total / rounds:.1f}.")
    else:
        print("В этом забеге боёв не было.")


# --- Заголовок ------------------------------------
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
while True:
    try:
        try:
            health = int(input())
            strength = int(input())
            agility = int(input())
            luck = int(input())
        except ValueError:
            raise ValueError("Ой: одна из строк не число")
        if health <= 0:
            raise ValueError(f"Здоровье должно быть положительным, а введено {health}")
        if strength < 0 or agility < 0 or luck < 0:
            raise ValueError("Характеристики не могут быть отрицательными")
        break
    except ValueError as e:
        print(f"{e}. Введите все четыре снова:")

# --- Расчёт урона ---------------------------------
damage = base_attack + strength * 1.5
crit_damage = damage * 2
stamina = health // 10 + luck
max_health = health
max_stamina = stamina

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
menu_last = 9
running = True
actions = 0
outcome = "прерывание"

try:
    while running:
        print("Что делаешь?")
        print("1 - осмотреться")
        print("2 - идти вперёд")
        print("3 - отдохнуть")
        print("4 - постучать по стене")
        print("5 - зажечь фонарь")
        print("6 - тренировка")
        print("7 - спуск вниз")
        print("8 - лидерборд")
        print("9 - магазин")
        print("0 - выйти из рудника")
        while True:
            choice = input()
            try:
                menu_number = int(choice)
            except ValueError:
                print("Такого пункта нет. Введи номер пункта из меню.")
                continue
            if 0 <= menu_number <= menu_last:
                break
            print("Такого пункта нет. Введи номер пункта из меню.")
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
                    hit_damage = hero_hit(i)
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
            case "7":
                if not enemies:
                    print("Ты спускаешься по лестнице, но рудник пуст — врагов больше нет.")
                else:
                    enemy = random.choice(enemies)
                    print(f"Ты спускаешься по лестнице. Из темноты выходит {enemy}!")
                    rounds, won, health, loot = fight(enemy, health, bonus=ability_bonus)
                    for r in rounds:
                        log.append(r)
                    if won:
                        gold_total += loot
                        enemies.remove(enemy)
                        print(f"{enemy.capitalize()} побеждён! Врагов осталось: {len(enemies)}. Трофеи: {loot} золота.")
                        print(f"Бой: {len(rounds)} раундов.")
                    else:
                        print(f"Бой: {len(rounds)} раундов.")
            case "8":
                print_leaderboard(log)
            case "9":
                print("Магазин:")
                print("1 - зелье (+10 здоровья): 10 золота")
                print("2 - масло (+5 сил): 15 золота")
                print("3 - эликсир (+2 к урону до конца забега): 40 золота")
                print("Номер предмета (0 — не покупать):")
                item = input()
                prices = (10, 15, 40)
                names = ("зелье", "масло", "эликсир")
                if item in ("1", "2", "3"):
                    price = prices[int(item) - 1]
                    name = names[int(item) - 1]
                    print("Количество (Enter — одна штука):")
                    qty_line = input()
                    if qty_line == "":
                        qty = 1
                        gold_total, ok = buy(price, gold_total)
                    else:
                        qty = int(qty_line)
                        gold_total, ok = buy(price, gold_total, quantity=qty)
                    if ok:
                        if item == "1":
                            health = min(health + 10 * qty, max_health)
                        elif item == "2":
                            stamina = min(stamina + 5 * qty, max_stamina)
                        else:
                            ability_bonus += 2 * qty
                        print(f"Куплено: {qty} шт. {name} за {price * qty} золота. Осталось: {gold_total}.")
                    else:
                        print(f"Не хватает золота: нужно {price * qty}, есть {gold_total}.")
                elif item != "0":
                    print("Такого товара нет в магазине.")
            case "0":
                print("Ты поднимаешься по лестнице к свету. Рудник остаётся позади.")
                outcome = "выход"
                running = False
        if running:
            actions += 1
        print()
        print(f"Здоровье: {health}  Запас сил: {stamina}  Врагов осталось: {len(enemies)}  Золото: {gold_total}")
        if health <= 0:
            print(f"{hero_name} падает без сил. Рудник забирает ещё одного искателя.")
            outcome = "гибель"
            running = False
except KeyboardInterrupt:
    print()
    print("Игрок прервал сеанс.")
finally:
    print(frame)
    if outcome == "гибель":
        print(f"Ты не дошёл, {hero_name}. Действий совершено: {actions}.")
    elif outcome == "выход":
        print(f"Забег окончен, {hero_name}. Действий совершено: {actions}.")
    else:
        print(f"Сеанс прерван, {hero_name}. Действий совершено: {actions}.")
    print_run_summary(log)
    print(frame)
