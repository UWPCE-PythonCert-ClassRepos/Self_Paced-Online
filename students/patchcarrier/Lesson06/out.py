import sys
import io

a = io.StringIO()
sys.stdout = a
print('hi')
print('ho')
print('hey')

sys.stdout = sys.__stdout__
a.seek(0)

myset = {name[:-1] for name in a}
print(myset)

set2 = set()
a.seek(0)
name = a.readline()
while name:
    set2.add(name)
    name = a.readline()

print(set2)