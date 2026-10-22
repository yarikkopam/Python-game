import importlib.metadata
import sys
from pathlib import Path

base = Path(__file__).parent

try:
    colorama_version = importlib.metadata.version("colorama")
except importlib.metadata.PackageNotFoundError:
    colorama_version = "not installed"

print(f"venv: {sys.prefix != sys.base_prefix}")
print(f"colorama: {colorama_version}")
print(f"requirements: {(base / 'requirements.txt').read_text(encoding='utf-8').strip()}")
print(f"gitignore: {'.venv/' in (base / '.gitignore').read_text(encoding='utf-8')}")
