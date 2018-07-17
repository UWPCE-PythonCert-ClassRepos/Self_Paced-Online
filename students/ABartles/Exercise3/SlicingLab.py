
def first_last(seq):
    f = seq[:1]
    m = seq[1:len(seq)-1]
    l = seq[len(seq)-1:]
    newseq = l + m + f
    return newseq

def every_other(seq):
    newseq = seq[::2]
    return newseq

def mid_every_other(seq):
    mid = seq[4:len(seq)-4]
    newseq = every_other(mid)
    return newseq

def my_reversed(seq):
    i = 1
    while i <= len(seq):
        if i == 1:
            newseq = seq[len(seq)-i:]
        else:
            newseq = newseq + seq[len(seq)-i:len(seq)-i+1]
        i += 1
    return newseq

def thirds(seq):
    thirdish = len(seq) // 3
    first = seq[:thirdish]
    mid = seq[thirdish:thirdish*2]
    last =  seq[thirdish*2:]
    newseq = mid + last + first
    return newseq

def test():
    a_string = "Oh the things you can find, if you dont stay behind!"
    a_list = [*range(1,21)]
    a_tuple = "start", 1,2,3,4,5,"middle",6,7,8,9,10,"End"

    assert first_last(a_string) == "!h the things you can find, if you dont stay behindO"
    assert every_other(a_string)== "O h hnsyucnfn,i o otsa eid"
    assert mid_every_other(a_string) == "h hnsyucnfn,i o otsa e"
    assert my_reversed(a_string) == "!dniheb yats tnod uoy fi ,dnif nac uoy sgniht eht hO"
    assert thirds(a_string) == " can find, if you dont stay behind!Oh the things you"

    assert first_last(a_list) == [20, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1]
    assert every_other(a_list) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    assert mid_every_other(a_list) == [5, 7, 9, 11, 13, 15]
    assert my_reversed(a_list) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert thirds(a_list) == [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6]

    assert first_last(a_tuple)== ('End', 1, 2, 3, 4, 5, 'middle', 6, 7, 8, 9, 10, 'start')
    assert every_other(a_tuple) == ('start', 2, 4, 'middle', 7, 9, 'End')
    assert mid_every_other(a_tuple) == (4, 'middle', 7)
    assert my_reversed(a_tuple) == ('End', 10, 9, 8, 7, 6, 'middle', 5, 4, 3, 2, 1, 'start')
    assert thirds(a_tuple) == (4, 5, 'middle', 6, 7, 8, 9, 10, 'End', 'start', 1, 2, 3)
    print("All assertions passed.")