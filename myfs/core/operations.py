import os
import errno
from time import time
from fuse import FuseOSError, Operations
from ..utils.path_utils import normalize_path
from .storage import MemoryStorage

class MemoryFS(Operations):
    def __init__(self, storage=None):
        self.storage = storage or MemoryStorage()
        self.fd = 0
        
    def create(self, path, mode):
        normalized_path = normalize_path(path)
        return self.storage.create_file(normalized_path, mode)
