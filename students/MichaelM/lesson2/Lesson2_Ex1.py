# cd C:\Users\v-micmcd.Redmond\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson2
# cd C:\Users\geekw\Dropbox\UW_Python\git\Self_Paced-Online\students\MichaelM\lesson2
# git status
# git add Lesson2_Ex1.py
# git commit
# git push
# goto https://github.com/geekwriter2/Self_Paced-Online/tree/master/students
# click Pull request > new pull request
# import name_main
# run Lesson2_Ex1.py
import random # import randint
def horizontalLine(boxCnt):
    print((('+' + '- - - - -') * int(boxCnt) ), end='+' + '\n')
def vertLine(boxCnt):
    cols = int(boxCnt) + 1
    print(((('|' + '         ') * cols)+ '\n') * 4, end='') 
    
def StackOBox(boxCntCols, boxCntRows):
    if (float(boxCntCols)).is_integer() & (float(boxCntRows)).is_integer():
        for _ in range(int(boxCntRows)):
            horizontalLine(boxCntCols)
            vertLine(boxCntCols)
        horizontalLine(boxCntCols)
    else:
        print("Oops... needed a whole number")
  

if __name__ == "__main__":
    threeSidedDie = round(random.uniform(0,.2), 1)
    cols = 7 + threeSidedDie
    rows = 4.0
    StackOBox(cols, rows)
    if (float(cols)).is_integer() & (float(rows)).is_integer():
         txt = '\n' + 'No more boxes (' + str(threeSidedDie) + ')...'
    else:
        txt = 'No boxes for you (' + str(threeSidedDie) + ')...'
    print(txt)



