# Part 3 assignment multi-dimension grid print hcount
import sys
def frame_proc():
    print("Frame Generator Processing Function Called")
    f = int(input("Enter Desired Grid Frame Size : "))
    if f <= 0:
        print ("You entered Zero. This is Not going to be much of a grid!")
        pass
    print("Horzontal Processing Function Called . . .")
    h = int(input("Enter Desired Horzontal Grid Frames: "))
    print("Vertical Processing Function Called . . .")
    v = int(input("Enter Desired Vertical Grid Frames: "))
    p = int(input("Enter Desired Padding - default is Grid Frame size: "))
    frame = f
    vcount = v
    hcount = h
    drawcount = vcount * frame
    pad = p
    print("Start Drawing...")
    print(hcount,vcount,frame,'h,v,frame')
    #initialize frame sizing
    for i in range (hcount):
        print(plus, minus * frame, end=' ')
        hcount = hcount -1
        if hcount == 0:
            print(plus)
            hcount = h
    while vcount >=1:
        for i in range (hcount):
            print(right_pipe, space4* frame, end=' ')
            hcount = hcount -1
            if hcount == 0:
                print(left_pipe)
                hcount = h
        vcount = vcount -1
    for i in range (hcount):
        print(plus, minus * frame, end=' ')
        hcount = hcount -1
        if hcount == 0:
            print(plus)
            hcount = h
    print("\n"+"How does it look? Use Padder to fix alignment!")
#Graph Symbols
plus = "+"
mid_plus = ' + '
minus = ' - '
space = ''
space1 = ' '
space2 = '  '
space3 = '   '
space4 = '    '
space5 = '     '
pipe = '|'
right_pipe = " |"
left_pipe = "| "
frame_proc()
