# -*- coding: utf-8 -*-
import colorama
from os import chdir, system
from os.path import basename
from datetime import datetime
import platform


colorama.init(autoreset=True)


def clear_console():
	if 'Windows' == platform.system():
		system('CLS')

	else:
		system('clear')
  
def show_example_of_use(file):
    clear_console()
    printOK(f'Example of use by {basename(file)[:-3]}\n\n', False)


def printOK(strOutput: str, showDate: str=True):
	timeStamp = f"{datetime.now().strftime('%H:%M:%S')} " if showDate else ""
	print(colorama.Style.BRIGHT + colorama.Fore.GREEN + '{}{}'.format(timeStamp, strOutput) +
	      colorama.Back.RESET + colorama.Fore.RESET)


def printBad(strOutput: str, showDate: str=True):
	timeStamp = f"{datetime.now().strftime('%H:%M:%S')} " if showDate else ""
	print(colorama.Style.BRIGHT + colorama.Fore.RED + '{}{}'.format(timeStamp, strOutput) +
            colorama.Back.RESET + colorama.Fore.RESET + colorama.Style.RESET_ALL)


def printWarning(strOutput: str, showDate: str=True):
	timeStamp = f"{datetime.now().strftime('%H:%M:%S')} " if showDate else ""
	print(colorama.Style.BRIGHT + colorama.Fore.YELLOW + '{}{}'.format(timeStamp, strOutput) +
            colorama.Back.RESET + colorama.Fore.RESET + colorama.Style.RESET_ALL)


def printShow(strOutput: str, showDate: str=True):
	timeStamp = f"{datetime.now().strftime('%H:%M:%S')} " if showDate else ""
	print(colorama.Style.BRIGHT + colorama.Fore.BLUE + '{}{}'.format(timeStamp, strOutput) +
            colorama.Back.RESET + colorama.Fore.RESET + colorama.Style.RESET_ALL)


if __name__ == '__main__':
	show_example_of_use(__file__)

	printOK('Mensaje')
	printBad('Mensaje')
	printWarning('Mensaje')
	printShow('Mensaje')
