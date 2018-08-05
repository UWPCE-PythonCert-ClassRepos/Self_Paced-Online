spth = "C:\\Users\\Andrew Bartles\\Desktop\\Self_Paced-Online\\students\\ABartles\\Exercise4\\Source"
dpth = C:\Users\Andrew Bartles\Desktop\Self_Paced-Online\students\ABartles\Exercise4\Destination


import pathlib

pth = pathlib.Path("./")
pth = pth.absolute()

for f in pth.iterdir():
    fp = pth / f
    print(fp)



for f in pth.iterdir():
    fp = pth / f
    print(fp)

    y = input()