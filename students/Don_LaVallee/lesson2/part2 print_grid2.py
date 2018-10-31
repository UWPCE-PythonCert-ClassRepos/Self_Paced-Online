# Part 1 catenation, multiplication of strings
plus = "+"
mid_plus = ' + '
minus = ' - '
space = ' '
space2 = '  '
space5 = "     "
pipe = "|"
right_pipe = " |"
left_pipe = "| "
print("\n")
i = int(input("Enter Desired Grid Frame Size: "))
if i <= 0:
    print ("You entered Zero. This is Not going to be much of a grid!")
    pass
sizer = i
padder = 1
vertical = 2
horizontal = i
rowcount = sizer * 2
procount = rowcount
midcount = procount / 2
if i <=1:
    padder = 2 + i
elif i <= 3:
     padder = 3 + i
else:
    padder = 2 * i
print("Start Drawing")
print(plus,minus*i,plus,minus*i,plus)
while  rowcount >= 0:
    while (procount) >= 0:
        print(pipe,space2*padder,pipe,space2*padder,pipe)
        procount = procount -1
        if (midcount) == (procount):
            print(plus,minus*i,plus,minus*i,plus)
    rowcount = rowcount - 1
print(plus,minus*i,plus,minus*i,plus)
print("How does it look?")
