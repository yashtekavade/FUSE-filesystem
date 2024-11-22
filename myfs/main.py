#!/usr/bin/env python3
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
