# wk: cd C:\Users\v-micmcd.Redmond\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson2
# mo: cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson2
# hm: cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson2
# run Lesson2_Ex3_Series.py
# git status
# git add Lesson2_Ex3_Series.py
# git add series.py
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
    n_minus2 = randint(0, 2)
    n_minus1 = 1
    # assertions test
    # n_minus2 = 1.5
    if n_minus2 == 0:
        calc_type = "Fibonacci"
    elif n_minus2 == 2:
        calc_type = "Lucas"
    else:
        calc_type = "currently undefined"
    check_inputs = series.assert_correct_input(n, n_minus2, n_minus1)
    if check_inputs != "ok":
        error_statement = "Incorrect input. Did you enter whole numbers only? ({:s}).".format(check_inputs)
        print(error_statement)
    else:
        series.sum_series(n, n_minus2=0, n_minus1=1)
        series_value = series.sum_series(n, n_minus2, 1)
        result = "The {:s} sequence term requested is {:d}. The value is: {}.".format(calc_type, n, series_value)
        print(result)


