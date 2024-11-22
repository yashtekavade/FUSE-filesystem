import os

def normalize_path(path):
    """Normalize filesystem paths"""
    return os.path.normpath(path)

def split_path(path):
    """Split path into directory and filename"""
    return os.path.split(normalize_path(path))
