__version__ = "$Version: 0.2.0"

from Crypto.Hash import SHA512
from os.path import exists
from os.path import getsize


def compare_files(original_file: str, compared_file: str, show_messages: bool = False):
    content_file = b''
    content_compared_file = b''

    if exists(original_file) and exists(compared_file):
        size_origin = getsize(original_file)
        size_target = getsize(compared_file)

        if size_origin == size_target:
            if size_origin > 0:
                with open(original_file, 'rb') as file:
                    content_file = file.read()

                with open(compared_file, 'rb') as file:
                    content_compared_file = file.read()

                hash_file = SHA512.new(content_file)
                hash_mirror = SHA512.new(content_compared_file)

                return hash_file.digest() == hash_mirror.digest()
            else:
                if show_messages:
                    print('Both are zero lenght')

                return True
        else:
            if show_messages:
                print('The size is different')

            return False

    else:
        if show_messages:
            print('One or both are not exists')

        return False
