# wk: cd C:\Users\v-micmcd.Redmond\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson2
# mo: cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson2
# hm: cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson2
# run Lesson2_Ex3_Series.py
# git status
# git add Lesson2_Ex3_Series.py
# git commit
# git push
# goto https://github.com/geekwriter2/Self_Paced-Online/tree/master/students/MichaelM/lesson2/
# click Pull request > new pull request
# from Natasha: python uses snake_case, verify indentation, convention is to use 4 spaces

import series
from random import randint
import importlib
importlib.reload(series)

if __name__ == "__main__":
    n = randint(0, 9)
    fib_calc = series.fibonacci(n)
    lucas_calc = series.lucas(n)
    checkwork_fib = "0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610"
    checkwork_Luc = "2, 1, 3, 4, 7, 11, 18, 29 //first 8"
    result = "The fibonacci and lucas sequence term requested is {:d}. The Fibonacci value is: {:d}. The Lucas value is: {:d}".format(
        n, fib_calc, lucas_calc)
    print(result)
    print(checkwork_fib)
    print(checkwork_Luc)
