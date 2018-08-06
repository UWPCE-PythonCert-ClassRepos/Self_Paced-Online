import pathlib

pth = pathlib.Path("./")
pth = pth.absolute()

for f in pth.iterdir():
    fp = pth / f
    print(fp)

y = input()