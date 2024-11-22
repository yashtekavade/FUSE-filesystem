#!/usr/bin/env python3
import os
import stat

def create_directory(path):
    """Create directory if it doesn't exist"""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")

def create_file(path, content=""):
    """Create file with given content"""
    with open(path, 'w') as f:
        f.write(content)
    print(f"Created file: {path}")
    
    # Make the file executable if it's a .py file
    if path.endswith('.py'):
        st = os.stat(path)
        os.chmod(path, st.st_mode | stat.S_IEXEC)

def setup_project():
    # Project root directory
    project_name = "myfs"
    create_directory(project_name)
    
    # Create project structure
    directories = [
        'core',
        'utils',
        'config',
        'tests',
    ]
    
    # Create all directories
    for dir_name in directories:
        dir_path = os.path.join(project_name, dir_name)
        create_directory(dir_path)
        create_file(os.path.join(dir_path, '__init__.py'))
    
    # Create main __init__.py
    create_file(os.path.join(project_name, '__init__.py'))
    
    # Create core files
    core_files = {
        'operations.py': '''import os
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
''',
        'storage.py': '''from collections import defaultdict
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
''',
        'errors.py': '''class FSError(Exception):
    """Base class for filesystem errors"""
    pass

class FileNotFoundError(FSError):
    """Raised when a file operation is requested on a non-existent file"""
    pass
'''
    }
    
    for filename, content in core_files.items():
        create_file(os.path.join(project_name, 'core', filename), content)
    
    # Create utils files
    utils_files = {
        'path_utils.py': '''import os

def normalize_path(path):
    """Normalize filesystem paths"""
    return os.path.normpath(path)

def split_path(path):
    """Split path into directory and filename"""
    return os.path.split(normalize_path(path))
''',
        'logging_utils.py': '''import logging

def setup_logger(name, level=logging.INFO):
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(level)
    return logger
'''
    }
    
    for filename, content in utils_files.items():
        create_file(os.path.join(project_name, 'utils', filename), content)
    
    # Create config files
    config_content = '''# Configuration settings for the filesystem
FILESYSTEM_CONFIG = {
    'block_size': 512,
    'total_blocks': 4096,
    'max_file_size': 1024 * 1024 * 10,  # 10MB
    'max_filename_length': 255
}
'''
    create_file(os.path.join(project_name, 'config', 'settings.py'), config_content)
    
    # Create test files
    test_content = '''import unittest
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
'''
    create_file(os.path.join(project_name, 'tests', 'test_operations.py'), test_content)
    
    # Create main.py
    main_content = '''#!/usr/bin/env python3
import sys
from fuse import FUSE
from core.operations import MemoryFS
from utils.logging_utils import setup_logger

def main():
    if len(sys.argv) != 2:
        print('Usage: {} <mountpoint>'.format(sys.argv[0]))
        sys.exit(1)
    
    logger = setup_logger('myfs')
    logger.info('Starting filesystem...')
    
    fuse = FUSE(
        MemoryFS(),
        sys.argv[1],
        foreground=True,
        allow_other=True
    )

if __name__ == '__main__':
    main()
'''
    create_file(os.path.join(project_name, 'main.py'), main_content)
    
    # Create requirements.txt
    requirements_content = '''fusepy==3.0.1
pytest==7.3.1
'''
    create_file(os.path.join(project_name, 'requirements.txt'), requirements_content)
    
    # Create README.md
    readme_content = '''# MyFS - FUSE Filesystem Implementation

A simple in-memory filesystem implementation using FUSE.

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the filesystem:
   ```bash
   python main.py /path/to/mountpoint
   ```

## Testing

Run tests using pytest:
```bash
pytest tests/
```

## Project Structure

- `core/`: Core filesystem implementation
- `utils/`: Helper utilities
- `config/`: Configuration settings
- `tests/`: Unit tests
'''
    create_file(os.path.join(project_name, 'README.md'), readme_content)

if __name__ == "__main__":
    setup_project()
    print("\nProject setup complete! Next steps:")
    print("1. cd myfs")
    print("2. pip install -r requirements.txt")
    print("3. python main.py /path/to/mountpoint")