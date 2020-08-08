__version__ = "$Version: 1.0.0"


import colorama
from datetime import datetime


def print_color(string_output: str, type: str, show_date: str = True):
    timeStamp = f"{datetime.now().strftime('%H:%M:%S')} " if show_date else ""

    if type == 'bad':
        print(
            colorama.Style.BRIGHT + colorama.Fore.RED +
            '{}{}'.format(timeStamp, string_output) +
            colorama.Back.RESET +
            colorama.Fore.RESET +
            colorama.Style.RESET_ALL
        )
    elif type == 'ok':
        print(
            colorama.Style.BRIGHT +
            colorama.Fore.GREEN +
            '{}{}'.format(timeStamp, string_output) +
            colorama.Back.RESET +
            colorama.Fore.RESET
        )
    elif type == 'show':
        print(
            colorama.Style.BRIGHT +
            colorama.Fore.BLUE +
            '{}{}'.format(timeStamp, string_output) +
            colorama.Back.RESET +
            colorama.Fore.RESET +
            colorama.Style.RESET_ALL
        )
    elif type == 'warning':
        print(
            colorama.Style.BRIGHT +
            colorama.Fore.YELLOW +
            '{}{}'.format(timeStamp, string_output) +
            colorama.Back.RESET +
            colorama.Fore.RESET +
            colorama.Style.RESET_ALL
        )
    elif type == 'show':
        print(
            colorama.Style.BRIGHT +
            colorama.Fore.BLUE +
            '{}{}'.format(timeStamp, string_output) +
            colorama.Back.RESET +
            colorama.Fore.RESET +
            colorama.Style.RESET_ALL
        )
    else:
        print(f"I don't know type: {type}")
