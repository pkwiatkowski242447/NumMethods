import math
import os


def clear():
    if os.name == 'posix':
        os.system('clear')      # Czyszczenie konsoli dla systemów Linux / Mac
    else:
        os.system('cls')        # Czyszczenie konsoli dla systemu Windows


def round_value(val):
    if val > 0 and val - math.floor(val) >= 0.5:
        return math.floor(val) + 1
    elif val > 0 and val - math.floor(val) < 0.5:
        return math.floor(val)
    elif val < 0 and val - math.floor(val) <= 0.5:
        return math.floor(val)
    else:
        return math.floor(val) + 1


def power(val, exp):
    return 0
