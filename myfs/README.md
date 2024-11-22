# MyFS - FUSE Filesystem Implementation

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
