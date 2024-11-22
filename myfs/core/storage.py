from collections import defaultdict
from time import time
import os

class MemoryStorage:
    def __init__(self):
        self.files = {}
        self.data = defaultdict(bytes)
        self.created = time()
    
    def create_file(self, path, mode):
        self.files[path] = {
            'st_mode': mode,
            'st_nlink': 1,
            'st_size': 0,
            'st_ctime': time(),
            'st_mtime': time(),
            'st_atime': time(),
            'st_uid': os.getuid(),
            'st_gid': os.getgid()
        }
        return True
