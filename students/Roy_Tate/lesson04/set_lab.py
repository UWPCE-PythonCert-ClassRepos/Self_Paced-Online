

set2 = set([])
set3 = set([])
set4 = set([])

max = 20
for i in range(1, max +1):
    if i % 4 == 0:
        set4.add(i)
    if i % 3 == 0:
        set3.add(i)
    if i % 2 == 0:
        set2.add(i)

print('set2: ' + str(set2))
print('set3: ' + str(set3))
print('set4: ' + str(set4))
print(set2.issubset(set4))
print(set3.issubset(set4))
print(set4.issubset(set2))