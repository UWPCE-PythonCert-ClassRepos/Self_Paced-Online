import pathlib

source = 'test.txt'
dest = 'test2.txt'

pth = pathlib.Path('./')
#print(pth.absolute())

for file in pth.iterdir():
    print(file)

#with open(source, 'w') as f:
#    f.write("This is a test!")

with open(source, 'rb') as infile, open(dest, 'wb') as outfile:
        outfile.write(infile.read())