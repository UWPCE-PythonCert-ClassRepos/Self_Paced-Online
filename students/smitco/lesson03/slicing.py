#lesson 03 slicing lab

intro = "hello my name is courtney"

#first and last exchanged
def swap(seq):
    return seq[-1:] + seq[1:-1] + seq[0:1]

print(swap(intro))
print()
print()

#every other item removed
def step(seq):
    return seq[::2]

print(step(intro))
print()
print()

#first 4 and last 4 removed then every other in between
def chop(seq):
    return seq[4:-4:2]

print(chop(intro))
print()
print()

#middle third, last third, first third
def switch(seq):
    l = len(seq)//3
    return seq[l:-l] + seq[-l:] + seq[:l]
    
print(switch(intro))
print()
print()

#test section
teststring = "testing testing 123"
testtuple = (22, 12, 18, 13, 11, 2, 1)

assert swap(teststring) == "3esting testing 12t"
assert step(teststring) == "tsigtsig13"
assert chop(teststring) == "igtsig"
assert switch(teststring) == "g testing 123testin"

assert swap(testtuple) == (1, 12, 18, 13, 11, 2, 22)
assert step(testtuple) == (22, 18, 11, 1)
assert chop(testtuple) == ()
assert switch(testtuple) == (18, 13, 11, 2, 1, 22, 12)