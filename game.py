# ================================================
# ИГРА «ЗАБЫТЫЙ РУДНИК»
# Автор: Александров Ярослав
# Дата: октябрь 2026
#
# Забег сохраняется в save.json при выходе и прерывании,
# продолжается при следующем запуске. Гибель стирает
# сохранение. Команда «заново» выбрасывает сохранение.
# Кортежи и множества превращаются в списки при записи
# и обратно при чтении: JSON их не знает.
# ================================================

import json
import os
import random

import dungeon

try:
    from colorama import Fore, Style, init
    init()
    COLOR = True
except ImportError:
    COLOR = False

# --- Правила игры ---------------------------------
title = "ЗАБЫТЫЙ РУДНИК"
frame = "=" * 20

base_attack = 10

enemies = ["гуль", "скелет", "паук", "нетопырь"]

MAP = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "#", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", ".", ".", ".", "#"],
    ["#", "#", "S", ".", "#"],
]
DIRECTIONS = {"север": (-1, 0), "юг": (1, 0), "запад": (0, -1), "восток": (0, 1),
              "north": (-1, 0), "south": (1, 0), "west": (0, -1), "east": (0, 1)}
LOOT = {(1, 1): "старая монета", (2, 3): "пыльное зелье", (3, 3): "самоцвет стража"}

log = []
gold_total = 0
ability_bonus = 0
inventory = {}
hero_r, hero_c = 4, 2
visited = {(4, 2)}
found_loot = set()

num_to_verb = {"1": "осмотр", "2": "вперед", "3": "отдых", "4": "стук",
               "5": "фонарь", "6": "тренировка", "7": "спуск", "8": "топ",
               "9": "магазин", "10": "рюкзак", "11": "выпить", "0": "выход"}
commands = ["осмотр", "вперед", "отдых", "стук", "фонарь", "тренировка",
            "спуск", "топ", "магазин", "рюкзак", "выпить зелье",
            "купить <предмет> [кол-во]", "карта", "разведка", "заново", "выход"]
MENU = ["Что делаешь? (номер или команда; помощь — справка)",
        "1 - осмотреться (осмотр)",
        "2 - идти вперёд (вперед) / шаг: вперед <север|юг|запад|восток>",
        "3 - отдохнуть (отдых)",
        "4 - постучать по стене (стук)",
        "5 - зажечь фонарь (фонарь)",
        "6 - тренировка (тренировка)",
        "7 - спуск вниз (спуск)",
        "8 - лидерборд (топ)",
        "9 - магазин (магазин)",
        "10 - рюкзак (рюкзак)",
        "11 - выпить зелье (выпить)",
        "карта - показать карту, разведка - обойти карту, заново - новый забег",
        "0 - выйти из рудника (выход)"]


# --- Функции сюжета -------------------------------

def scout(r, c, seen):
    """Рекурсивно считает доступные комнаты от (r, c).

    seen — множество посещённых этим обходом. Выход за край,
    стена и повтор — базовый случай (вклад 0).
    Возвращает число доступных комнат.
    """
    if not (0 <= r < len(MAP) and 0 <= c < len(MAP[r])):
        return 0
    if (r, c) in seen or MAP[r][c] == "#":
        return 0
    seen.add((r, c))
    total = 1
    for dr, dc in set(DIRECTIONS.values()):
        total += scout(r + dr, c + dc, seen)
    return total


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


def write_save():
    """Собирает состояние забега и пишет его в save.json.

    Кортежи и множества превращает в списки: JSON их не знает.
    Возвращает None.
    """
    save = {}
    save["hero"] = hero_name
    save["health"] = health
    save["stamina"] = stamina
    save["max_health"] = max_health
    save["max_stamina"] = max_stamina
    save["strength"] = strength
    save["agility"] = agility
    save["luck"] = luck
    save["damage"] = damage
    save["crit_damage"] = crit_damage
    save["gold"] = gold_total
    save["actions"] = actions
    save["ability_bonus"] = ability_bonus
    save["inventory"] = inventory
    save["enemies"] = enemies
    save["position"] = [hero_r, hero_c]
    save["visited"] = [list(p) for p in visited]
    save["loot"] = sorted(found_loot)
    with open("save.json", "w", encoding="utf-8") as f:
        json.dump(save, f, ensure_ascii=False, indent=2)


# --- Заголовок ------------------------------------
print(frame)
print("   " + title + "   ")
print(frame)
print()

# --- Загрузка сохранения --------------------------
loaded = None
if os.path.exists("save.json"):
    print("Найдено сохранение. Продолжить забег? (да/нет)")
    answer = input().strip().lower()
    if answer in ("да", "yes"):
        try:
            with open("save.json", encoding="utf-8") as f:
                loaded = json.load(f)
        except Exception:
            print("Сохранение испорчено. Начинаю новый забег.")
            loaded = None

if loaded is None:
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

    running = True
    actions = 0
    outcome = "прерывание"
else:
    hero_name = loaded["hero"]
    health = loaded["health"]
    stamina = loaded["stamina"]
    max_health = loaded["max_health"]
    max_stamina = loaded["max_stamina"]
    strength = loaded["strength"]
    agility = loaded["agility"]
    luck = loaded["luck"]
    damage = loaded["damage"]
    crit_damage = loaded["crit_damage"]
    gold_total = loaded["gold"]
    actions = loaded["actions"]
    ability_bonus = loaded.get("ability_bonus", 0)
    inventory = loaded.get("inventory", {})
    enemies = loaded["enemies"]
    hero_r, hero_c = loaded["position"]
    visited = {tuple(p) for p in loaded["visited"]}
    found_loot = set(loaded["loot"])
    print(f"Забег продолжен: здоровье {health}, золото {gold_total}, врагов осталось {len(enemies)}.")
    running = True
    outcome = "прерывание"

# --- Главный цикл игры ----------------------------
try:
    while running:
        print("\n".join(MENU))
        print()
        line = input()
        cmd = line.strip().lower()
        while cmd == "":
            print("Пустая команда. Введи команду или номер.")
            line = input()
            cmd = line.strip().lower()
        words = cmd.split()
        verb = words[0]
        if cmd in num_to_verb:
            verb = num_to_verb[cmd]
        match verb:
            case "осмотр" | "осмотреться":
                print("Ты осматриваешься. В стенах старые следы кирки, на полу пыль.")
            case "вперед" | "идти":
                if len(words) > 1 and words[1] in DIRECTIONS:
                    dr, dc = DIRECTIONS[words[1]]
                    nr, nc = hero_r + dr, hero_c + dc
                    if 0 <= nr < len(MAP) and 0 <= nc < len(MAP[nr]) and MAP[nr][nc] != "#":
                        hero_r, hero_c = nr, nc
                        visited.add((hero_r, hero_c))
                        if (hero_r, hero_c) in LOOT:
                            item = LOOT[(hero_r, hero_c)]
                            if item not in found_loot:
                                found_loot.add(item)
                                print(f"Ты находишь: {item}! Уникальных находок: {len(found_loot)}.")
                        print(f"Ты шагаешь {words[1]}. Комната ({hero_r}, {hero_c}).")
                    else:
                        print(f"Туда не пройти ({words[1]}): стена или край.")
                else:
                    cost = 2
                    if stamina >= cost:
                        stamina -= cost
                        print("Ты осторожно идёшь вперёд. Гравий хрустит под ногами.")
                    else:
                        health -= cost - stamina
                        stamina = 0
                        print("Сил больше нет — ты идёшь на одном упорстве.")
            case "отдых" | "отдохнуть":
                stamina += 3
                print("Ты садишься на груду досок и переводишь дух. Силы возвращаются.")
            case "стук" | "постучать":
                print("Ты стучишь по стене. Где-то в глубине эхо отвечает глухим раскатом.")
            case "фонарь" | "свет":
                stamina -= 1
                print("Ты зажигаешь фонарь. Дрожащий свет вытягивает из темноты стены рудника.")
            case "тренировка":
                strikes = 6
                train_cost = 4
                total_damage = 0
                crit_count = 0
                print("Ты подходишь к тренировочной глыбе.")
                print("Её оставил здесь прошлый рудокоп — для разминки перед спуском.")
                print()
                print(f"Наносите {strikes} ударов.")
                for i in range(1, strikes + 1):
                    hit_damage, crit = dungeon.hero_hit(i, damage, crit_damage)
                    if crit:
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
            case "спуск" | "вниз":
                if not enemies:
                    print("Ты спускаешься по лестнице, но рудник пуст — врагов больше нет.")
                else:
                    enemy = random.choice(enemies)
                    print(f"Ты спускаешься по лестнице. Из темноты выходит {enemy}!")
                    rounds, won, health, loot = dungeon.fight(enemy, health, ability_bonus, damage, crit_damage)
                    for r in rounds:
                        log.append(r)
                    if won:
                        gold_total += loot
                        enemies.remove(enemy)
                        win_line = f"{enemy.capitalize()} побеждён! Врагов осталось: {len(enemies)}. Трофеи: {loot} золота."
                        if COLOR:
                            print(Fore.YELLOW + win_line + Style.RESET_ALL)
                        else:
                            print(win_line)
                        print(f"Бой: {len(rounds)} раундов.")
                    else:
                        print(f"Бой: {len(rounds)} раундов.")
            case "топ" | "лидерборд":
                print_leaderboard(log)
            case "магазин":
                print("Магазин:")
                for name, price in dungeon.prices.items():
                    print(f"{name}: {price} золота")
            case "купить" | "buy":
                if len(words) > 1 and words[-1].isdigit():
                    qty = int(words[-1])
                    item = " ".join(words[1:-1])
                else:
                    qty = 1
                    item = " ".join(words[1:])
                if item == "":
                    print("Купить что? Введи: купить <предмет>.")
                    continue
                if item not in dungeon.prices:
                    print("Такого товара нет в магазине.")
                    continue
                gold_total, ok = dungeon.buy(dungeon.prices[item], gold_total, quantity=qty)
                if ok:
                    inventory[item] = inventory.get(item, 0) + qty
                    if item == "эликсир":
                        ability_bonus += 2 * qty
                    print(f"Куплено: {qty} шт. {item} за {dungeon.prices[item] * qty} золота. Осталось: {gold_total}.")
                else:
                    print(f"Не хватает золота: нужно {dungeon.prices[item] * qty}, есть {gold_total}.")
            case "рюкзак":
                if not inventory:
                    print("Рюкзак пуст.")
                else:
                    print("Рюкзак:")
                    for name, qty in inventory.items():
                        print(f"{name}: {qty} шт.")
            case "выпить" | "пить" | "drink":
                item = " ".join(words[1:]) or "зелье"
                if inventory.get(item, 0) == 0:
                    print(f"В рюкзаке нет: {item}.")
                else:
                    health = min(health + 10, max_health)
                    inventory[item] -= 1
                    if inventory[item] == 0:
                        del inventory[item]
                    print(f"Ты выпиваешь {item}. Здоровье: {health}. Осталось: {inventory.get(item, 0)} шт.")
            case "карта" | "map":
                print("Карта:")
                for i in range(len(MAP)):
                    cells = []
                    for j in range(len(MAP[i])):
                        cell = "@" if (i, j) == (hero_r, hero_c) else MAP[i][j]
                        cells.append(cell)
                    print(" ".join(cells))
            case "разведка" | "scout":
                seen = set()
                print(f"Разведка: доступно комнат: {scout(hero_r, hero_c, seen)}.")
            case "заново" | "newgame":
                if os.path.exists("save.json"):
                    os.remove("save.json")
                    print("Сохранение стёрто. Следующий забег начнётся заново.")
                else:
                    print("Сохранения нет — нечего стирать.")
                continue
            case "помощь" | "help":
                print("Команды: " + ", ".join(commands) + ".")
                print("Номера 0-11 работают как раньше.")
            case "выход" | "выйти" | "exit":
                print("Ты поднимаешься по лестнице к свету. Рудник остаётся позади.")
                write_save()
                print("Прогресс сохранён.")
                outcome = "выход"
                running = False
            case _:
                print(f"Не понимаю команду: '{line.strip()}'. Введи 'помощь'.")
                continue
        if running:
            actions += 1
        print()
        state = f"Здоровье: {health}  Запас сил: {stamina}  Врагов осталось: {len(enemies)}  Золото: {gold_total}"
        if COLOR:
            print(Fore.GREEN + state + Style.RESET_ALL)
        else:
            print(state)
        if health <= 0:
            print(f"{hero_name} падает без сил. Рудник забирает ещё одного искателя.")
            if os.path.exists("save.json"):
                os.remove("save.json")
            outcome = "гибель"
            running = False
except KeyboardInterrupt:
    print()
    print("Игрок прервал сеанс.")
    write_save()
finally:
    print(frame)
    if outcome == "гибель":
        print(f"Ты не дошёл, {hero_name}. Действий совершено: {actions}.")
    elif outcome == "выход":
        print(f"Забег окончен, {hero_name}. Действий совершено: {actions}.")
    else:
        print(f"Сеанс прерван, {hero_name}. Действий совершено: {actions}.")
    print_run_summary(log)
    if inventory:
        print("В рюкзаке осталось:")
        for name, qty in inventory.items():
            print(f"{name}: {qty} шт.")
    else:
        print("В рюкзаке осталось: пусто.")
    print(frame)
