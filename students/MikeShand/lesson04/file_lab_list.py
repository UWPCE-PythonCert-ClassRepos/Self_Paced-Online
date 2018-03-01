import pathlib

for file in pathlib.WindowsPath().rglob("*"):
    print(file.absolute())
