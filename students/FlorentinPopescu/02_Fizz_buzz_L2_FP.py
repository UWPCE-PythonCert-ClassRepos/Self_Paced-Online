# -*- coding: utf-8 -*-
"""
Created on Thu Jan 3 20:17:15 2019
@author: Florentin Popescu
"""

#=============LESSON_02====================
#-------------Fizz-Buzz exercise ----------
#==========================================

# Option 1 - using a for loop and conditionals 
import time
start_time = time.time()

for i in range(1, 101):
    if (i % 3 == 0) and (i % 5 == 0):
        print('FizzBuzz')
    elif i % 3 == 0: 
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else: print(i)

print("--- %s seconds ---" % (time.time() - start_time))
#-------------------------------------------

# Option 2 - using a while loop and conditionals 
import time
start_time = time.time()

i = 1
while i < 101:
    if (i % 3 == 0) and (i % 5 == 0):
        print('FizzBuzz')
    elif i % 3 == 0: 
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else: print(i)
    i += 1

print("--- %s seconds ---" % (time.time() - start_time))
#-------------------------------------------

# Option 3 - concatenating strings 
import time
start_time = time.time()

for i in range(1,101):
    st = ' '
    if i % 3 == 0:
        st += 'Fizz'
    if i % 5 == 0:
        st += 'Buzz'
    if i % 5 != 0 and i % 3 != 0:
        st += str(i)
    print(st)

print("--- %s seconds ---" % (time.time() - start_time))
#-------------------------------------------

# Option 4 - using list comprehension
import time
start_time = time.time()

print("\n".join(["Fizz"*(i%3==0) + "Buzz"*(i%5==0) or str(i) for i in range(1,101)]))

print("--- %s seconds ---" % (time.time() - start_time))
#--------------------------------------------

#Option 5 - using NumPy and Pandas
import time
start_time = time.time()

import numpy as np
import pandas as pd

s0 = pd.DataFrame([i for i in np.arange(1, 101) if ((i % 3 != 0) 
                   and (i % 5 != 0) and (i % 15 != 0))], columns = ['idx'])
s0['name'] = s0['idx']

s1 = pd.DataFrame([i for i in np.arange(1, 101) if i % 3 == 0 
                   and i % 5 != 0], columns = ['idx'])
s1['name'] = 'Fizz'

s2 = pd.DataFrame([i for i in np.arange(1, 101) if i % 5 == 0 
                   and i % 3 != 0], columns = ['idx'])
s2['name'] = 'Buzz'

s3 = pd.DataFrame([i for i in np.arange(1, 101) if i % 3 == 0 
                   and i % 5 == 0], columns = ['idx'])
s3['name'] = 'FizzBuzz'

print(s0.append(s1.append(s2.append(s3))).set_index('idx').sort_index()['name'].reset_index(drop = True))

print("--- %s seconds ---" % (time.time() - start_time))
#-------------------------------------------

#===========================================
# END
#===========================================