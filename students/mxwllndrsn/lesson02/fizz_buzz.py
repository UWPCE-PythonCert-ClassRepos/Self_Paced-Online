#uw python 210
#lesson 02
#max anderson

# fizzin and a buzzin
# for fun you can select which multiples get fizzed/buzzed
# defaults to 3 and 5 per assignment

def fizz_buzz(a=3, b=5):

    for i in range(100):

        #clear n
        n = ''

        if i % a == 0:
            n += 'fizz'
            if i % b == 0:
                n += 'buzz'
        elif i % b == 0:
            n += 'buzz'
        else:
            n = i

        if i == 0:
            pass
        else:
            print(n)