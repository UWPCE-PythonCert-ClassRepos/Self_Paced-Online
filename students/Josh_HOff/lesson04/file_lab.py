import pathlib
#print(os.listdir())
pth = pathlib.Path('./')
p = pth.absolute()
for i in pth.iterdir():
    print(f'{p}\{i}')
f = open('test.txt')

with open('test.txt', 'w') as outfile:
    outfile.write('hello2')

while True:
    line = f.readline()
    if not line:
        print(5)
        break