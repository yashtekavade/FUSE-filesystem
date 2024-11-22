class FSError(Exception):
    """Base class for filesystem errors"""
    pass

class FileNotFoundError(FSError):
    """Raised when a file operation is requested on a non-existent file"""
    pass
