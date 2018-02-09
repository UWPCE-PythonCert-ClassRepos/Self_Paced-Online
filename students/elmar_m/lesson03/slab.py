a = "this is a string"
t = (2, 54, 13, 12, 5, 32)

'''
first and last element exchanged: 
'''

def exfl(a):
   # print(a[-1] + a[1:-1] + a[0])
   return a[-1] + a[1:-1] + a[0]


'''
every other item except first and last removed:
'''
def onlyfl(a):
    return a[:1] + a[-1:]

'''
with the first 4 and the last 4 items removed, and then every other item in between
'''
def withoutfl4(a):
    return a[4:-4]

'''
with the elements reversed:
'''
def rev(a):
    return a[::-1]

'''
with the middle third, then last third, then the first third in the new order.
'''
def third(a):
    # thrd = len(a) // 3
    n = len(a) // 3
    return a[n:-n] + a[-n:] + a[:n]


'''
Assertions:
'''
# assert exchange_first_last(a) == "ghis is a strint"
assert exfl(a) == "ghis is a strint"
# assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
assert exfl(t) == (32, 54, 13, 12, 5, 2)


if __name__ == '__main__':
    print('I dont wanna be executed directly, please import me as a module!')
