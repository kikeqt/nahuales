__version__ = "$Version: 0.0.1"

from Crypto.Hash import SHA512


def compare_files(original_file: str, mirror_file: str):
    content_file = None
    content_mirror = None
    
    with open(original_file, 'r') as file:
        content_file = file.read()
        
    with open(content_mirror, 'r') as file:
        content_mirror = file.read()
        
    hash_file = SHA512.new(content_file)
    hash_mirror = SHA512.new(content_mirror)
    
    return hash_file.digest() == hash_mirror.digest()