#manually create box
def printing():
     plus = '+ '
     minus = '- '
     pipe = '| '
     space = ' '
     print(plus + (minus*4) + plus + (minus*4) + plus)
     print(pipe + space*8 +pipe+ space*8 +pipe)
     print(pipe + space*8 +pipe+ space*8 +pipe)
     print(pipe + space*8 +pipe+ space*8 +pipe)
     print(pipe + space*8 +pipe+ space*8 +pipe)
     print(plus + (minus*4) + plus + (minus*4) + plus)
     print(pipe + space*8 +pipe+ space*8 +pipe)
     print(pipe + space*8 +pipe+ space*8 +pipe)
     print(pipe + space*8 +pipe+ space*8 +pipe)
     print(pipe + space*8 +pipe+ space*8 +pipe)
     print(plus + (minus*4) + plus + (minus*4) + plus)


def dynamicprinting(x):
     #check if x=1 - can't do this grid
     if x==1:
          Print("Too small to make a grid")
     borders = 2 + 1 #2 outer borders and 1 inner
     #border@ 0, x+1, and x*2-1
     #fixes even entries into odd to match EX(8)
     xfix = x+1 if x % 2 == 0 else x
     grid_height = int(1/2 * xfix) #  also used round(1/2 * x)
     total_w = xfix * 2 + borders # 15 * 2 + 3 
     total_h = grid_height * 2 + borders
     dashes = ''
     pipes = ''

     #create lines with plus and dashes
     for i in range(total_w):
          if i == 0:
               dashes += '+'
          elif i == int(total_w/2):
               dashes += '+'
          elif i == total_w-1:
               dashes += '+'
          elif i % 2 == 0 :
               dashes += '-'
          else:
               dashes += ' '

     #create line with pipes
     pipes = '|' + ' '* xfix + '|' + ' '* xfix + '|'

     #print entire grid
     for g in range(total_h):
          if g == 0 or g == total_h-1:
               print(dashes)
          elif g == int(total_h/2):
               print(dashes)
          else:
               print(pipes)


def printgrid(gridsize, units):
      #check if x=1 - can't do this grid
     
     borders = gridsize + 1
     
     width = units * 2 + 1
     #grid_height = int(1/2 * unitsfix) #  also used round(1/2 * x)
     total_w = width * gridsize + borders # 9 * 3 + 4 
     total_h = units  * gridsize + borders #2*3+5
     dashes = ''
     pipes = ''

     #create lines with plus and dashes
     for i in range(total_w):
          if i == 0 or i == total_w-1:
               dashes += '+'
               pipes += '|'
          elif i % (width+1) == 0:
               dashes += '+'
               pipes += '|'
          elif i % 2 == 0 :
               dashes += '-'
               pipes += ' '
          else:
               dashes += ' '
               pipes += ' '


     #print entire grid
     for g in range(total_h):
          if g == 0 or g == total_h-1:
               print(dashes)
          elif g % (units+1) == 0:
               print(dashes)
          else:
               print(pipes)

def box():
     size = 5
     inner_size = size - 2
     print ('*' * size)
     for i in range(inner_size):
         print ('*' + ' ' * inner_size + '*')
     print ('*' * size)
     