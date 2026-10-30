from pathlib import Path

content : Path = Path(".")

files  = [file for file in content.iterdir() if file.is_file()]
print(files)