try:
    from colorama import Fore, Style, init
    init()
    COLOR = True
except ImportError:
    COLOR = False

state = "Health: 90 Stamina: 14 Enemies left: 3 Gold: 25"

if COLOR:
    print(Fore.GREEN + state + Style.RESET_ALL)
else:
    print(state)
