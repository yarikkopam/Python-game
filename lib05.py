try:
    from colorama import Fore, Style, init
    init()
    COLOR = True
except ImportError:
    COLOR = False

win_line = "skeleton defeated! 3 enemies left in the dungeon. Loot: 25 gold."

if COLOR:
    print(Fore.MAGENTA + win_line + Style.RESET_ALL)
    print(Fore.RED + "critical" + Style.RESET_ALL, Fore.BLUE + "loot" + Style.RESET_ALL)
    print(Style.DIM + "dim" + Style.RESET_ALL, Style.BRIGHT + "bright" + Style.RESET_ALL)
else:
    print(win_line)
    print("critical loot")
    print("dim bright")
