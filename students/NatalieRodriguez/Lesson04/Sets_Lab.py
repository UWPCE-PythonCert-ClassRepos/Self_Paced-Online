#$ chmod +x dict_lab.py

#Lesson 04: Sets Labs
#Natalie Rodriguez
# March 31, 2018

#Sets 1

s2 = set(range(0, 21, 2))
s3 = set(range(0, 21, 3))
s4 = set(range(0, 21, 4))

print('s2 =', s2, '\n')
print('s3 =', s3, '\n')
print('s4 =', s4, '\n')

print('s3 is subset of s2:', s3.issubset(s2), '\n')
print('s4 is subset of s2:', s4.issubset(s2), '\n')

#Sets 2

P = set()
P.update('Python')
P.add('i')
print(P)

frozen = frozenset('marathon')

print('Union of two sets =', P.union(frozen), '\n')
print('Intersection of two sets =', P.intersection(frozen), '\n')