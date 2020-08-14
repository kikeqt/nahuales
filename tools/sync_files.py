__version__ = "$Version: 0.0.1"

from os.path import exists as exists_path
from os import remove
from shutil import copyfile

from .compare_files import compare_files


def sync_files(source_file: str, target_file: str, show_messages: bool = False):
    if not exists_path(source_file):
        if exists_path(target_file):
            if show_messages:
                print(f'Remove: {target_file}')

            remove(target_file)
            return 'remove target'

        else:
            if show_messages:
                print(f'Not exists any file {source_file}')

            return 'there is none'

    else:
        return_state = ''

        if not compare_files(source_file, target_file):
            if exists_path(target_file):
                if show_messages:
                    print(f'Replace file: {target_file}')
                    
                return_state = 'replace'

                remove(target_file)

            else:
                if show_messages:
                    print(f'Copy file: {source_file}')
                
                return_state = 'copy'

        else:
            if show_messages:
                print(f'The files are equals')
                
            return_state = 'are equal'

        copyfile(source_file, target_file)
        
        return return_state
