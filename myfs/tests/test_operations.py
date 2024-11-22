import unittest
from ..core.operations import MemoryFS
from ..core.storage import MemoryStorage

class TestMemoryFS(unittest.TestCase):
    def setUp(self):
        self.fs = MemoryFS(MemoryStorage())
    
    def test_create_file(self):
        path = '/test.txt'
        mode = 0o644
        fd = self.fs.create(path, mode)
        self.assertGreater(fd, 0)
