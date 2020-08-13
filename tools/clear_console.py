__version__ = "$Version: 0.2.1"

from os import system
import platform


def clear_console():
    if 'Windows' == platform.system():
        system('CLS')

    else:
        system('clear')


if __name__ == '__main__':
    clear_console()
