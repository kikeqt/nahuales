__version__ = "$Version: 0.0.1"

from os.path import basename

from .clear_console import clear_console
from .print_color import print_color


def show_example_of_use(file):
    clear_console()
    print_color(f'Example of use by {basename(file)[:-3]}\n', type= 'ok', show_date= False)

