__version__ = "$Version: 1.0.1"

from .files import Files
from tools import Integer_2_bytes


class Test_Files(object):
    __current_file = 0
    __test_files = []
    __truncated_path = "benchmark/truncated_folder/"
    __my_test_files = (
        # PNG files
        {'file_location': 'benchmark/data/Logo_Kike.png', 'category': 'png', },
        {'file_location': 'benchmark/data/Glider.png', 'category': 'png', },
        {'file_location': 'benchmark/data/PNG_demo.png', 'category': 'png',
            'url_file': 'https://es.wikipedia.org/wiki/Portable_Network_Graphics#/media/Archivo:PNG_transparency_demonstration_1.png', },

        # JPG files
        {'file_location': 'benchmark/data/Manglar.jpg', 'category': 'jpg', },
        {'file_location': 'benchmark/data/tepoztlan.jpg', 'category': 'jpg', },
        {'file_location': 'benchmark/data/flower.jpg', 'category': 'jpg', },

        # Small random binary files
        {'file_location': 'benchmark/data/VeraCrypt.key', 'category': 'rand bin', },
        {'file_location': 'benchmark/data/VeraCrypt_1.key', 'category': 'rand bin', },
        {'file_location': 'benchmark/data/VeraCrypt_2.key', 'category': 'rand bin', },

        # Plain text
        {'file_location': 'benchmark/data/el_quijote.txt', 'category': 'Plain text',
            'url_file': 'https://gist.githubusercontent.com/jsdario/6d6c69398cb0c73111e49f1218960f79/raw/8d4fc4548d437e2a7203a5aeeace5477f598827d/el_quijote.txt', },
        {'file_location': 'benchmark/data/la_Odisea.txt', 'category': 'Plain text',
            'url_file': 'http://www.gutenberg.org/files/58221/58221-0.txt'},
        {'file_location': 'benchmark/data/the_Iliad.txt', 'category': 'Plain text',
            'url_file': 'http://www.gutenberg.org/files/22382/22382-0.txt'},

        # Monotone text from sts-2_1_2.zip
        {'file_location': 'benchmark/data/data.pi',
            'category': 'Monotone text from sts-2_1_2.zip', },
        {'file_location': 'benchmark/data/data.e',
            'category': 'Monotone text from sts-2_1_2.zip', },
        {'file_location': 'benchmark/data/sqrt2.bin',
            'category': 'Monotone text from sts-2_1_2.zip', },

        # PDF files
        {'file_location': 'benchmark/data/Analysis2005.pdf', 'category': 'PDF files',
            'url_file': 'https://www.random.org/analysis/Analysis2005.pdf', },
        {'file_location': 'benchmark/data/nist_sp800-22r1a.pdf', 'category': 'PDF files',
            'url_file': 'https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-22r1a.pdf', },
        {'file_location': 'benchmark/data/librotmed.pdf', 'category': 'PDF files',
            'url_file': 'http://matematicas.unex.es/~ricarfr/librotmed.pdf', },

        # ZIP files
        {'file_location': 'benchmark/data/Fast_NIST_STS_v6.0.1.zip', 'category': 'Zip files',
            'url_file': 'https://github.com/sysox/NIST-STS-optimised/files/4052762/Fast_NIST_STS_v6.0.1.zip'},
        {'file_location': 'benchmark/data/sts-2_1_2.zip', 'category': 'Zip file',
            'url_file': 'https://csrc.nist.gov/CSRC/media/Projects/Random-Bit-Generation/documents/sts-2_1_2.zip'},
        {'file_location': 'benchmark/data/CRYPTOPP_5_6_5.zip', 'category': 'Zip file',
            'url_file': 'https://github.com/weidai11/cryptopp/archive/CRYPTOPP_5_6_5.zip'},
    )

    def __init__(self):
        for item in self.__my_test_files:
            self.__test_files.append(Files(**item))

        self.__truncate_files()

    def __truncate_files(self):
        for item in range(len(self.__test_files)):
            self.__test_files[item].truncated_path = self.__truncated_path
            self.__test_files[item].generate_truncated_file()

    def get_files_iterative(self):
        for item in self.__test_files:
            yield item

    def get_keys_iterative(self):
        integer_2_bytes = Integer_2_bytes()

        for key in range(256):
            yield integer_2_bytes.integer_2_bytes(key)
