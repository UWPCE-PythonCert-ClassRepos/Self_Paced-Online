def gd3(h, w, csize):
    for i in range(1, (h + 1) + (h * csize) + 1):
        if i % (csize + 1) == 1:
            print(w * ('+ ' + csize * ('- ')) + '+')
        else:
            print(w * ('| ' + (2 * csize) * ' ') + '|')

            
 