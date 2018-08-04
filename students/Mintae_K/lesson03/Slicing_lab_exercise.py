def slicing_exercise(x):
    print(x)
    s= x[-1:] + x[1:-1] + x[0:1]
    print ("with the first and last items exchanged:",s)
    #next
    s = x[::2]
    print ("with every other item removed:",s)
    #next
    s = x[4:-4:2]
    print ("first 4, last 4 removed, and every other item in between:",s)
    #next
    s = x[::-1]
    print ("with the elements reversed (just with slicing):",s)
    #next
    third = int(len(x)/3)
    s = x[third:-third] + x[-third:] + x[:third]
    print ("with the middle third, then last third, then first third:",s)
    return
