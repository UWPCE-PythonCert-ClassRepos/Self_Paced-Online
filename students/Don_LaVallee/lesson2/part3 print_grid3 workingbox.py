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
    p = 6
    p = int(input("Enter Desired Padding - default is Grid Frame size: "))
    if p <= 0:
        print ("You entered an invalid value. Defaulting set to 1x1x1")
        f=1
        h=1
        v=1
        p = 2
        pass
    elif h <= 1:
        p = p + 1
        pass
    elif h <= 2:
        p = frame
    elif h >= 3:
        p = f * p
        pass
    frame = f
    vcount = v
    hcount = h
    format = (frame + hcount) + p
    pad = p + format
    drawcount = vcount
    print('Padding is currently set to = ', pad)
    print("Start Drawing Dynamic Grid Matrix ...")
    print(frame, hcount,vcount,pad,'= frame, horizontal, vertical, padding')
    #initialize frame sizing
    for i in range (hcount):
        #print the  header row
        print(plus, minus * frame, end=' ')
        hcount = hcount -1
        if hcount == 0:
            print(plus)
            hcount = h
    for i in range (drawcount):
        #print grid blocks to entered value dimensions
        while drawcount >=1:
            for i in range (vcount):
                print(pipe, space1 * pad, end=' ')
                hcount = hcount -1
                if hcount == 0:
                    print(pipe)
                    hcount = h
                    vcount = vcount -1
                if vcount == 0:
                    for i in range (hcount):
                        print(plus, minus * frame, end=' ')
                        hcount = hcount -1
                        if hcount == 0:
                            print(plus)
                            hcount = h
                            vcount = v
                            drawcount = drawcount -1
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
