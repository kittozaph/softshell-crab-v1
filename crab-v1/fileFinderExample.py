from pathlib import Path

path = Path('crab-v1/images/test.txt')

if path.is_file():
    print("File found at", path)
else:
    print("File not found")