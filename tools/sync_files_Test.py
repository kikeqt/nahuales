__version__ = "$Version: 0.0.1"

from unittest import TestCase
from os import mkdir
from os.path import exists
from shutil import rmtree

from .sync_files import sync_files


class Sync_files_Test(TestCase):

    def test_sync_files(self):
        path_test = 'temp/'
        path_origin = 'temp/origin/'
        path_target = 'temp/target/'

        if exists(path_test):
            rmtree(path_test)

        mkdir(path_test)
        mkdir(path_origin)
        mkdir(path_target)

        with open(f'{path_target}delete_file', 'w') as file:
            file.write('anything')

        with open(f'{path_origin}only_source', 'w') as file:
            file.write('anything')
            
        with open(f'{path_origin}for_replace', 'w') as file:
            file.write('anything')
            
        with open(f'{path_target}for_replace', 'w') as file:
            file.write('anything else')

        dict_test = [
            {
                'origin_file': f'{path_origin}does_not_exist',
                'target_file': f'{path_target}does_not_exist',
                'result': 'there is none'
            },
            {
                'origin_file': f'{path_origin}delete_file',
                'target_file': f'{path_target}delete_file',
                'result': 'remove target'
            },
            {
                'origin_file': f'{path_origin}only_source',
                'target_file': f'{path_target}only_source',
                'result': 'copy'
            },
            {
                'origin_file': f'{path_origin}only_source',
                'target_file': f'{path_target}only_source',
                'result': 'are equal'
            },
            {
                'origin_file': f'{path_origin}for_replace',
                'target_file': f'{path_target}for_replace',
                'result': 'replace'
            },
        ]

        for item in dict_test:
            self.assertEqual(
                item['result'],
                sync_files(item['origin_file'], item['target_file']))

        rmtree(path_test)
