_version_ = "$Version: 0.0.3"

import json
from os.path import exists
from shutil import copytree
from typing import Dict
from typing import Union
import zipfile

from .files import Files
from tools import sync_files


class Fast_NIST_STS_Maker(object):
    _version_sts = ''
    _base_path = 'benchmark/'
    _environment_unzip = ''
    _environment_location = 'benchmark/sts/'
    _config: Dict[str, Dict[str, Union[str, Dict[str,str]]]] = {}

    def __init__(self, version_sts: str):
        self._version_sts = version_sts

        self._load_from_JSON()
        self._get_tool()
        self._setup_environment()

    def _load_from_JSON(self):
        with open(f'{self._base_path}/config_sts.json', 'r') as file_json:
            self._config = file_json.read()

        self._config = json.loads(self._config)

    def _get_tool(self):
        file_location = self._config[self._version_sts]['file_location']
        url_file = self._config[self._version_sts]['url_file']
        self._environment_unzip = self._base_path + \
            self._config[self._version_sts]['fftw']['with']
        self._bin = self._config[self._version_sts]['bin']
        self._dll = self._config[self._version_sts]['dll']

        # Download file if not exists
        _ = Files(file_location=file_location, url_file=url_file)

        # Unzip file
        if not exists(self._environment_unzip):
            print(f'Unzip: {file_location}')
            
            with zipfile.ZipFile(file_location, "r") as zip_ref:
                zip_ref.extractall(self._base_path)
                
    def _setup_environment(self):
        # If not exists FFTW (Fastest Fourier Transform in the West) binary
        # replace it
        if not exists(self._environment_unzip + self._bin):
            self._environment_unzip = self._base_path + \
                self._config[self._version_sts]['fftw']['without']

        # Verify path environment
        if not exists(self._environment_location + self._bin):
            print(f'Create dir: {self._environment_location}')
            copytree(self._environment_unzip, self._environment_location, dirs_exist_ok=True)
            
        sync_files(
            self._environment_unzip + self._bin,
            self._environment_location + self._bin)
        
        sync_files(
            self._environment_unzip + self._dll,
            self._environment_location + self._dll)
